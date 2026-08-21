# 🎓 Academix / College Attendance Tracker

> \*\*Smart, Automated College Attendance \& Analytics Platform\*\*

\---

## 📌 Problem Statement

Traditional college attendance tracking via manual roll calls or paper sheets is time-consuming, prone to proxy attendance, and lacks real-time visibility for students and administrators. Students often struggle to track their threshold warnings (e.g., falling below 75%), leading to unexpected exam detentions.

\---

## 💡 Solution

An automated, role-based attendance management system designed for university departments. It simplifies class logging for professors, provides real-time attendance analytics for students, and automatically flags low-attendance warnings before mandatory thresholds are breached.

\---

## ✨ Key Features

* **Multi-Role Portals:** Separate dashboards for Students, Faculty, and Admin/HODs.
* **Rapid Session Marking:** Single-click batch attendance recording for course coordinators.
* **Real-time Analytics Dashboard:** Visual progress tracking showing current attendance percentages and minimum classes needed to reach target thresholds (e.g., 75%).
* **Automated Defaulter Alerts:** Instant system flagging for students slipping below mandatory university criteria.
* **Exportable Reports:** One-click CSV/PDF attendance report generation for administrative audits.

\---

## 🛠️ Tech Stack

|Layer|Technologies|
|-|-|
|**Frontend**|React.js, Tailwind CSS|
|**Backend**|Node.js, Express.js|
|**Database**|MongoDB (Mongoose ORM)|
|**Authentication**|JWT (JSON Web Tokens), Bcrypt|

\---

## 🏗️ System Flow

```
\[ Professor ] ──► Marks Session ──► \[ Express Backend ] ──► \[ MongoDB ]
                                            │
                                            └──► Updates Student Analytics
                                            └──► Triggers Threshold Alert (If < 75%)
```

\---

## ⚡ Local Setup \& Installation

### Prerequisites

* Node.js (`v18+`)
* MongoDB (Local Instance or MongoDB Atlas)

### Step-by-Step Setup

1. **Clone the repository:**

```bash
   git clone <YOUR\_GITHUB\_REPO\_URL>
   cd college-attendance-app
   ```

2. **Install Dependencies:**

```bash
   # Server dependencies
   cd server \&\& npm install

   # Client dependencies
   cd ../client \&\& npm install
   ```

3. **Configure Environment Variables:**
Create a `.env` file in the `/server` directory:

```env
   PORT=5000
   MONGO\_URI=your\_mongodb\_connection\_string
   JWT\_SECRET=your\_jwt\_secret\_key
   ```

4. **Run Development Server:**

```bash
   # Start backend (from /server)
   npm run dev

   # Start frontend (from /client)
   npm start
   ```



\---

## 📄 License

Distributed under the MIT License.

