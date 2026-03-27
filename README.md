# ☁️ Cloud Security Copilot

An AI-powered cloud security and cost optimization dashboard that analyzes cloud infrastructure data, detects risks, and provides intelligent remediation insights using a hybrid AI architecture.

---

## 📌 Overview

Cloud Security Copilot is designed to help organizations identify security vulnerabilities, optimize cloud costs, and gain actionable insights from their cloud resource data.

The system combines **AI-powered analysis with a hybrid architecture**, ensuring reliability even when external AI APIs fail.

---

## 🔥 Key Features

- 🔍 **Security Risk Detection**
  - Identifies misconfigurations such as:
    - Publicly exposed resources
    - Excessive IAM permissions
    - Missing encryption

- 💰 **Cost Optimization**
  - Detects underutilized resources
  - Estimates potential cost savings (USD & INR)

- 📊 **Interactive Dashboard**
  - Risk overview (High / Medium / Low)
  - Visual analytics using charts

- 🤖 **AI Remediation Insights**
  - Generates intelligent suggestions for fixing issues

- 💬 **AI Copilot Assistant**
  - Ask questions about your cloud infrastructure

- 🧠 **Hybrid AI Architecture**
  - Uses **Gemini API** for advanced insights
  - Falls back to **RAG-based system** if API fails

---

## 🏗️ Architecture

This project follows a modular architecture:
User Upload → Data Processing → Security + Cost Analysis → Risk Scoring
→ AI Insight Generation (Gemini API / RAG Fallback) → Dashboard Output


---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|----------|
| Frontend UI | Streamlit |
| Backend     | Python |
| Data Handling | Pandas |
| Visualization | Plotly |
| AI Integration | Gemini API |
| Fallback AI | RAG (Retrieval-Augmented Generation) |

---

## 📂 Project Structure
│
├── dashboard/
│ └── app.py # Main Streamlit dashboard
│
├── engine/
│ ├── security_analysis.py
│ ├── cost_analysis.py
│ └── data_loader.py
│
├── utils/
│ ├── risk_scoring.py
│ └── report_generator.py
│
├── genai/
│ └── insight_generator.py
│
├── rag/
│ ├── rag_engine.py
│ └── copilot.py
│
├── data/
│ └── cloud_resources.csv
│
├── requirements.txt
└── README.md


---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/cloud-security-copilot.git
cd cloud-security-copilot/dashboard
2. Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Run the application
streamlit run app.py
📊 How It Works
Upload a CSV dataset containing cloud resources
System analyzes:
Security risks
Cost inefficiencies
Calculates risk scores
Generates:
Visual insights
AI recommendations
Allows interactive querying via Copilot
🧠 Hybrid AI System

This project implements a fault-tolerant AI pipeline:

Primary: Gemini API
Fallback: RAG-based system
Why this matters:
Handles API failures
Reduces dependency on external services
Improves reliability

🚀 Future Enhancements
Integration with AWS / Azure APIs
Real-time monitoring
Authentication system
Deployment on cloud (AWS / GCP)
Advanced analytics dashboard
👩‍💻 Author

Harshita Chabaria
B.Tech CSE | Cloud & AI Enthusiast

💡 Key Learnings
Cloud security fundamentals
Cost optimization strategies
AI integration in real-world systems
Hybrid architecture design
Building interactive dashboards
⭐ Conclusion

Cloud Security Copilot demonstrates how AI can simplify cloud infrastructure management by combining:

Security analysis
Cost optimization
Intelligent recommendations
Reliable hybrid AI systems
