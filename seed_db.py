import random
from database import get_db

db = get_db()

def seed_database():
    print("Seeding database...")
    
    # 1. Clear existing collections
    collections = ['students', 'faculty', 'sessions', 'courses', 'course_registrations', 'course_allotments', 'attendance_details', 'sent_email_details']
    for coll in collections:
        db[coll].drop()
        print(f"Dropped collection {coll}")

    # 2. Insert Students (Sapthagiri NPS University - CSE SEM 4)
    students_data = [
        {"id": 1,  "roll_no": "24SUUBECS1814", "name": "SAHARSH B S",              "email_id": "saharsh.bs@snpsu.edu.in"},
        {"id": 2,  "roll_no": "24SUUBECS1815", "name": "SAHARSH J",                "email_id": "saharsh.j@snpsu.edu.in"},
        {"id": 3,  "roll_no": "24SUUBECS1816", "name": "SAHEEGOUDA PATIL",          "email_id": "saheegouda.patil@snpsu.edu.in"},
        {"id": 4,  "roll_no": "24SUUBECS1817", "name": "SAI CHARAN",               "email_id": "sai.charan@snpsu.edu.in"},
        {"id": 5,  "roll_no": "24SUUBECS1818", "name": "SAI KIRAN REDDY G S",      "email_id": "saikiran.reddy@snpsu.edu.in"},
        {"id": 6,  "roll_no": "24SUUBECS1820", "name": "SAI VIGNESH R",            "email_id": "sai.vignesh@snpsu.edu.in"},
        {"id": 7,  "roll_no": "24SUUBECS1822", "name": "SAISH M KOTHARKAR",        "email_id": "saish.kotharkar@snpsu.edu.in"},
        {"id": 8,  "roll_no": "24SUUBECS1823", "name": "SAISRUSTI P H",            "email_id": "saisrusti.ph@snpsu.edu.in"},
        {"id": 9,  "roll_no": "24SUUBECS1824", "name": "SAI VIKAS VEERAPPA KAYKAD","email_id": "saivikas.kaykad@snpsu.edu.in"},
        {"id": 10, "roll_no": "24SUUBECS1825", "name": "SAJAL BRICHPURIA",         "email_id": "sajal.brichpuria@snpsu.edu.in"},
        {"id": 11, "roll_no": "24SUUBECS1828", "name": "SAKSHI S",                 "email_id": "sakshi.s@snpsu.edu.in"},
        {"id": 12, "roll_no": "24SUUBECS1831", "name": "SALLA GAGANA",             "email_id": "salla.gagana@snpsu.edu.in"},
        {"id": 13, "roll_no": "24SUUBECS1832", "name": "SAMANVITA",                "email_id": "samanvita@snpsu.edu.in"},
        {"id": 14, "roll_no": "24SUUBECS1833", "name": "SAMARTH",                  "email_id": "samarth@snpsu.edu.in"},
        {"id": 15, "roll_no": "24SUUBECS1835", "name": "SAMARTH CHIKKEGOWDA",      "email_id": "samarth.chikkegowda@snpsu.edu.in"},
        {"id": 16, "roll_no": "24SUUBECS1840", "name": "SAMEEKSHA P",              "email_id": "sameeksha.p@snpsu.edu.in"},
        {"id": 17, "roll_no": "24SUUBECS1842", "name": "SAMITH GOWDA R",           "email_id": "samith.gowda@snpsu.edu.in"},
        {"id": 18, "roll_no": "24SUUBECS1846", "name": "SAMRUDH S SHETTY",         "email_id": "samrudh.shetty@snpsu.edu.in"},
        {"id": 19, "roll_no": "24SUUBECS1847", "name": "SAMYUKTAA P",              "email_id": "samyuktaa.p@snpsu.edu.in"},
        {"id": 20, "roll_no": "24SUUBECS1848", "name": "SAMYUKTHA MENON",          "email_id": "samyuktha.menon@snpsu.edu.in"},
        {"id": 21, "roll_no": "24SUUBECS1849", "name": "SANA U B",                 "email_id": "sana.ub@snpsu.edu.in"},
        {"id": 22, "roll_no": "24SUUBECS1850", "name": "SANCHIT HARSHA M",         "email_id": "sanchit.harsha@snpsu.edu.in"},
        {"id": 23, "roll_no": "24SUUBECS1852", "name": "SANDEEP D",                "email_id": "sandeep.d@snpsu.edu.in"},
        {"id": 24, "roll_no": "24SUUBECS1853", "name": "SANDEEP KUMAR S",          "email_id": "sandeep.kumar@snpsu.edu.in"},
        {"id": 25, "roll_no": "24SUUBECS1856", "name": "SANGAMESH",                "email_id": "sangamesh@snpsu.edu.in"},
        {"id": 26, "roll_no": "24SUUBECS1858", "name": "SANGAMESH V",              "email_id": "sangamesh.v@snpsu.edu.in"},
        {"id": 27, "roll_no": "24SUUBECS1860", "name": "SANGEETHA S",              "email_id": "sangeetha.s@snpsu.edu.in"},
        {"id": 28, "roll_no": "24SUUBECS1862", "name": "SANIKA",                   "email_id": "sanika@snpsu.edu.in"},
        {"id": 29, "roll_no": "24SUUBECS1863", "name": "SANIKA K",                 "email_id": "sanika.k@snpsu.edu.in"},
    ]
    db.students.insert_many(students_data)
    print(f"Inserted {len(students_data)} students")

    # 3. Insert Faculty (Sapthagiri NPS University - CSE Dept)
    faculty_data = [
        {"id": 1, "user_name": "deepika",  "password": "deepika@123",  "name": "Deepika"},
        {"id": 2, "user_name": "veena",    "password": "veena@123",    "name": "Veena"},
        {"id": 3, "user_name": "pratap",   "password": "pratap@123",   "name": "Pratap"},
        {"id": 4, "user_name": "kavya",    "password": "kavya@123",    "name": "Kavya"},
    ]
    db.faculty.insert_many(faculty_data)
    print("Inserted faculty")

    # 4. Insert Sessions
    sessions_data = [
        {"id": 1, "year": 2026, "term": "SEM 4"},
    ]
    db.sessions.insert_many(sessions_data)
    print("Inserted sessions")

    # 5. Insert Courses (CSE SEM 4)
    courses_data = [
        {"id": 1, "title": "Discrete Mathematical Structures", "code": "CSE401", "credit": 4},
        {"id": 2, "title": "Data Analytics and Visualization", "code": "CSE402", "credit": 4},
        {"id": 3, "title": "Design and Analysis of Algorithms", "code": "CSE403", "credit": 4},
        {"id": 4, "title": "Database Management Systems",       "code": "CSE404", "credit": 4},
    ]
    db.courses.insert_many(courses_data)
    print("Inserted courses")

    # 6. Course Allotments — assign each faculty their course
    #    Deepika -> CSE401, Veena -> CSE402, Pratap -> CSE403, Kavya -> CSE404
    allotments = [
        {"faculty_id": 1, "course_id": 1, "session_id": 1},  # Deepika -> DMS
        {"faculty_id": 2, "course_id": 2, "session_id": 1},  # Veena   -> DAV
        {"faculty_id": 3, "course_id": 3, "session_id": 1},  # Pratap  -> DAA
        {"faculty_id": 4, "course_id": 4, "session_id": 1},  # Kavya   -> DBMS
    ]
    db.course_allotments.insert_many(allotments)
    print("Inserted course allotments")

    # 7. Register all students to all courses in session 1
    registrations = []
    for student in students_data:
        for course in courses_data:
            registrations.append({
                "student_id": student["id"],
                "course_id": course["id"],
                "session_id": 1
            })
    db.course_registrations.insert_many(registrations)
    print("Inserted course registrations")

    print("\nDatabase seeded successfully!")
    print("Faculty Login Credentials:")
    for f in faculty_data:
        print(f"  Username: {f['user_name']}  |  Password: {f['password']}")

if __name__ == "__main__":
    seed_database()
