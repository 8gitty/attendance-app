# ⚡ PlasmaGrid

> **Automated, Zero-Waste Resource Allocation & Routing Network**

---

## 📌 Problem Statement

Critical medical supplies, blood components, and emergency resources suffer from severe distribution imbalances. While central hub nodes often face expiring surpluses and operational waste, peripheral hospital nodes experience acute shortages due to slow, manual allocation systems and static routing models.

---

## 💡 Solution

**PlasmaGrid** is an intelligent resource redistribution platform that continuously detects surplus node inventory ("wasted" capacity) and calculates real-time optimal reallocation matrixes. It automatically determines:

1. **Exact Quota Allocation:** How many units to pull from high-surplus nodes without causing local deficits.
2. **Dynamic Transfer Routing:** The shortest, time-optimized distribution path between donor nodes and target recipient nodes using network routing algorithms.

---

## ✨ Key Features

* **Surplus Node Detection:** Automatically flags nodes approaching resource expiration or excess capacity threshold.
* **Smart Allocation Engine:** Calculates optimal N-node transfer matrices to eliminate local shortages with minimum trip cycles.
* **Optimized Route Planner:** Generates shortest time-to-transit path based on node distance, priority urgency, and transit constraints.
* **Real-time Inventory Ledger:** Tracks node state changes dynamically across supply, demand, and transit stages.

---

## 🛠️ Tech Stack

| Layer | Technologies |
| --- | --- |
| **Frontend** | React, Tailwind CSS |
| **Backend** | Node.js, Express.js |
| **Database** | MongoDB |
| **Routing / Engine** | Custom Optimization Algorithm, Leaflet / Mapbox API |

---

## 🏗️ Architecture & Allocation Logic

```
┌─────────────────────┐       ┌──────────────────────┐
│  Surplus Node (A)   │       │  Deficit Node (B)    │
│  (Excess Resources) │       │  (Critical Demand)   │
└──────────┬──────────┘       └──────────▲───────────┘
           │                             │
           └──► [ PlasmaGrid Engine ] ───┘
                ├── Calculates Optimal Transfer Quantity (ΔQ)
                └── Outputs Shortest Dynamic Route (A ──► B)
```

---

## ⚡ Local Setup & Installation

### Prerequisites
* Node.js (`v18+`)
* MongoDB (Local Instance or MongoDB Atlas)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd plasmagrid
   ```

2. **Install dependencies:**
   ```bash
   # Install server dependencies
   cd server && npm install

   # Install client dependencies
   cd ../client && npm install
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the `/server` directory:
   ```env
   PORT=5000
   MONGO_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret
   ```

4. **Run Locally:**
   ```bash
   # Run Backend (from /server)
   npm run dev

   # Run Frontend (from /client)
   npm start
   ```

---

## 👥 Team Members

* **Full-Stack / Core Devs** - *PlasmaGrid Development Team*

---

## 📄 License

Distributed under the MIT License.
