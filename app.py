from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from database import get_db

app = Flask(__name__)
app.secret_key = "attendance_super_secret_key"
db = get_db()

@app.route("/")
def index():
    if "current_user" in session:
        return redirect(url_for("attendance"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.json
        user_name = data.get("username")
        password = data.get("password")
        faculty = db.faculty.find_one({"user_name": user_name, "password": password})
        if faculty:
            session["current_user"] = faculty["id"]
            return jsonify({"status": "success"})
        return jsonify({"status": "error", "message": "Invalid credentials"})
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("current_user", None)
    return redirect(url_for("login"))

@app.route("/attendance")
def attendance():
    if "current_user" not in session:
        return redirect(url_for("login"))
    return render_template("attendance.html", facid=session["current_user"])

# API Routes
@app.route("/api/session", methods=["GET"])
def get_session():
    sessions = list(db.sessions.find({}, {"_id": 0}))
    return jsonify(sessions)

@app.route("/api/facultyCourses", methods=["POST"])
def get_faculty_courses():
    data = request.json
    facid = int(data.get("facid"))
    sessionid = int(data.get("sessionid"))
    
    # Get courses for this faculty in this session
    allotments = list(db.course_allotments.find({"faculty_id": facid, "session_id": sessionid}))
    course_ids = [a["course_id"] for a in allotments]
    courses = list(db.courses.find({"id": {"$in": course_ids}}, {"_id": 0}))
    return jsonify(courses)

@app.route("/api/studentList", methods=["POST"])
def get_student_list():
    data = request.json
    classid = int(data.get("classid"))
    sessionid = int(data.get("sessionid"))
    facid = int(data.get("facid"))
    ondate = data.get("ondate")
    
    # 1. Get all students registered for this course and session
    registrations = list(db.course_registrations.find({"course_id": classid, "session_id": sessionid}))
    student_ids = [r["student_id"] for r in registrations]
    students = list(db.students.find({"id": {"$in": student_ids}}, {"_id": 0}))
    
    # 2. Get attendance for this specific date
    attendance_records = list(db.attendance_details.find({
        "course_id": classid, 
        "session_id": sessionid,
        "faculty_id": facid,
        "on_date": ondate
    }))
    present_student_ids = [a["student_id"] for a in attendance_records if a["status"] == "YES"]
    
    # 3. Calculate total attendance classes (unique dates this faculty taught this class)
    all_attendance = list(db.attendance_details.find({
        "course_id": classid, 
        "session_id": sessionid,
        "faculty_id": facid
    }))
    unique_dates = set([a["on_date"] for a in all_attendance])
    total_classes = len(unique_dates)
    
    # Assemble response
    for student in students:
        student["isPresent"] = "YES" if student["id"] in present_student_ids else "NO"
        # Calculate attended classes
        attended = len([a for a in all_attendance if a["student_id"] == student["id"] and a["status"] == "YES"])
        student["attended"] = attended
        student["percent"] = round((attended / total_classes * 100), 2) if total_classes > 0 else 0

    return jsonify({"total": total_classes, "studentlist": students})

@app.route("/api/saveAttendance", methods=["POST"])
def save_attendance():
    data = request.json
    courseid = int(data.get("courseid"))
    sessionid = int(data.get("sessionid"))
    studentid = int(data.get("studentid"))
    facultyid = int(data.get("facultyid"))
    ondate = data.get("ondate")
    status = data.get("ispresent")
    
    # Upsert attendance record
    db.attendance_details.update_one(
        {
            "course_id": courseid,
            "session_id": sessionid,
            "student_id": studentid,
            "faculty_id": facultyid,
            "on_date": ondate
        },
        {"$set": {"status": status}},
        upsert=True
    )
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
