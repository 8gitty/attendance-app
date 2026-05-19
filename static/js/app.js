document.addEventListener('DOMContentLoaded', () => {
    const facid = document.getElementById('facid').value;
    const sessionSelect = document.getElementById('sessionSelect');
    const coursesGrid = document.getElementById('coursesGrid');
    const studentListContainer = document.getElementById('studentListContainer');
    const studentsWrapper = document.getElementById('studentsWrapper');
    const attendanceDate = document.getElementById('attendanceDate');
    const dateControl = document.getElementById('dateControl');
    const selectedCourseTitle = document.getElementById('selectedCourseTitle');
    const totalClassesBadge = document.getElementById('totalClassesBadge');

    let currentClassId = null;

    // Set today's date as default
    const today = new Date().toISOString().split('T')[0];
    attendanceDate.value = today;

    // Load Sessions
    fetch('/api/session')
        .then(res => res.json())
        .then(data => {
            data.forEach(s => {
                const opt = document.createElement('option');
                opt.value = s.id;
                opt.textContent = `${s.year} - ${s.term}`;
                sessionSelect.appendChild(opt);
            });
        });

    // Session Change Handler
    sessionSelect.addEventListener('change', (e) => {
        const sessionid = e.target.value;
        studentListContainer.style.display = 'none';
        dateControl.style.display = 'none';
        
        if (!sessionid) {
            coursesGrid.innerHTML = '';
            return;
        }

        fetch('/api/facultyCourses', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ facid, sessionid })
        })
        .then(res => res.json())
        .then(courses => {
            coursesGrid.innerHTML = '';
            courses.forEach(c => {
                const card = document.createElement('div');
                card.className = 'glass course-card';
                card.innerHTML = `
                    <h3>${c.code}</h3>
                    <p style="color: var(--text-muted); font-size: 0.875rem;">${c.title}</p>
                    <span style="display:inline-block; margin-top: 12px; font-size: 0.75rem; background: var(--primary-color); padding: 2px 8px; border-radius: 12px; color: white;">Credits: ${c.credit}</span>
                `;
                card.addEventListener('click', () => loadStudents(c.id, c.code + ' - ' + c.title));
                coursesGrid.appendChild(card);
            });
        });
    });

    // Date Change Handler
    attendanceDate.addEventListener('change', () => {
        if (currentClassId) loadStudents(currentClassId, selectedCourseTitle.textContent);
    });

    // Load Students
    function loadStudents(classid, title) {
        currentClassId = classid;
        selectedCourseTitle.textContent = title;
        studentListContainer.style.display = 'flex';
        dateControl.style.display = 'block';
        
        const sessionid = sessionSelect.value;
        const ondate = attendanceDate.value;

        studentsWrapper.innerHTML = '<div style="padding: 24px; text-align: center;">Loading...</div>';

        fetch('/api/studentList', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ classid, sessionid, facid, ondate })
        })
        .then(res => res.json())
        .then(data => {
            totalClassesBadge.textContent = `Total Classes: ${data.total}`;
            studentsWrapper.innerHTML = '';
            
            data.studentlist.forEach(student => {
                const row = document.createElement('div');
                row.className = 'student-row glass';
                row.style.borderTop = 'none';
                row.style.borderLeft = 'none';
                row.style.borderRight = 'none';
                row.style.borderRadius = '0';
                
                const isPresent = student.isPresent === 'YES';
                
                row.innerHTML = `
                    <div style="font-family: monospace; color: var(--text-muted);">${student.roll_no}</div>
                    <div>${student.name}</div>
                    <div style="text-align: center;">
                        <span style="color: ${student.percent < 75 ? 'var(--danger)' : 'var(--success)'}">${student.percent}%</span>
                        <div style="font-size: 0.7rem; color: var(--text-muted);">${student.attended}/${data.total}</div>
                    </div>
                    <div style="text-align: center; display: flex; justify-content: center; gap: 8px;">
                        <button class="attendance-toggle ${isPresent ? 'present' : ''}" data-status="YES" title="Mark Present">P</button>
                        <button class="attendance-toggle ${!isPresent ? 'absent' : ''}" data-status="NO" title="Mark Absent">A</button>
                    </div>
                `;

                // Add event listeners to toggle buttons
                const btns = row.querySelectorAll('.attendance-toggle');
                btns.forEach(btn => {
                    btn.addEventListener('click', (e) => {
                        const status = e.target.getAttribute('data-status');
                        saveAttendance(student.id, status, btns);
                    });
                });

                studentsWrapper.appendChild(row);
            });
        });
    }

    function saveAttendance(studentid, status, btns) {
        const sessionid = sessionSelect.value;
        const ondate = attendanceDate.value;

        fetch('/api/saveAttendance', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                courseid: currentClassId,
                sessionid,
                studentid,
                facultyid: facid,
                ondate,
                ispresent: status
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 'success') {
                // Update UI visually
                btns.forEach(b => {
                    b.classList.remove('present', 'absent');
                    if (b.getAttribute('data-status') === status) {
                        b.classList.add(status === 'YES' ? 'present' : 'absent');
                    }
                });
            }
        });
    }
});
