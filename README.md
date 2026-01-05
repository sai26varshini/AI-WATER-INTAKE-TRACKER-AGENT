💧 AI Water Tracker

An AI-powered Water Intake Tracking Application built using FastAPI, Streamlit, SQLite, and Groq LLM.
The app helps users log daily water intake, track hydration history, and receive AI-based hydration feedback in real time.

🧠 Features

✅ Dynamic user-based water intake tracking

✅ AI-generated hydration feedback using Groq LLM

✅ Persistent storage using SQLite

✅ Interactive dashboard with charts

✅ REST API with FastAPI

✅ Clean separation of frontend & backend

✅ Production-ready cloud deployment

🏗️ Tech Stack

| Layer      | Technology                                   |
| ---------- | -------------------------------------------- |
| Frontend   | Streamlit                                    |
| Backend    | FastAPI                                      |
| Database   | SQLite                                       |
| AI / LLM   | Groq (LLaMA 3.1)                             |
| Deployment | Render (Backend), Streamlit Cloud (Frontend) |
| Language   | Python 3.11                                  |

📂 Project Structure
WaterTracker/
│
├── src/
│   ├── api.py          # FastAPI routes
│   ├── agent.py        # AI hydration logic
│   ├── database.py     # SQLite DB operations
│   ├── logger.py       # Application logging
│
├── dashboard.py        # Streamlit frontend
├── requirements.txt
├── .gitignore
├── README.md
└── watertracker.db     # Created automatically (local only)

⚙️ Local Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/sai26varshini/AI-WATER-INTAKE-TRACKER-AGENT.git
cd watertracker

2️⃣ Create & activate virtual environment
python -m venv agent
agent\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the Application Locally
🔹 Start FastAPI backend
python -m uvicorn src.api:app --reload

open:
http://127.0.0.1:8000/docs

🔹 Start Streamlit frontend
python -m streamlit run dashboard.py

Open:
http://localhost:8501

☁️ Deployment Guide (Summary)
Backend (FastAPI)
Platform: Render
Start command:
python -m uvicorn src.api:app --host 0.0.0.0 --port 10000
Frontend (Streamlit)
Platform: Streamlit Cloud
Entry file: dashboard.py
