# 🛡️ INSA AI Engineering Capstone: Log Anomaly Detection & Threat Intelligence Copilot

**Student:** Eba Solomon | **Program:** INSA Summer Camp, 5th Batch (AI Engineering Track)

## 🌐 Live Demo
👉 **[Click here to test the Live Interactive SOC Dashboard](https://insa-log-triage-capstone.onrender.com)** 👈
*(Note: Hosted on Render's free tier. If the server is asleep, the first load may take 30–50 seconds).*

---

## 📌 Problem Statement
Security Operations Centers (SOCs) face severe **alert fatigue** due to high volumes of system logs and a high false-positive rate in basic detectors. Furthermore, modern AI models are often "black boxes"—when they flag an anomaly, analysts don't know *why*. 

This project solves this by providing an end-to-end pipeline that:
1. Detects anomalies using Machine Learning.
2. Maps threats to the **MITRE ATT&CK** framework.
3. Uses a **Retrieval-Augmented Generation (RAG)** knowledge base and a **Large Language Model (LLM)** to explain the anomaly and generate real-time mitigation checklists via an interactive chat.

---

## 🚀 Key Achievements & Architecture
- **Exploratory Data Analysis (EDA):** Cleaned and parsed raw HDFS logs, discovering a massive class imbalance (only 2% anomalies) that breaks standard accuracy metrics.
- **Machine Learning Pipeline:** Built a leak-proof `scikit-learn` pipeline using TF-IDF for text log templates and One-Hot Encoding for categorical features. Trained a `RandomForestClassifier` using `class_weight='balanced'` to prioritize catching rare anomalies.
- **Threat Intelligence (MITRE ATT&CK):** Automatically maps detected anomalies to known cybersecurity tactics (e.g., `T1565 - Data Manipulation`) to provide immediate context.
- **LLM-Powered SOC Copilot:** Integrated Llama-3 via the Groq API. When an anomaly is detected, the LLM generates a dynamic incident report. Analysts can then converse with the Copilot to get expert-level mitigation checklists (e.g., *"How do I fix this?"*).
- **Batch Processing:** Includes a high-volume CSV upload feature allowing analysts to process thousands of logs simultaneously.
- **MLOps & Deployment:** 
  - Packaged with **FastAPI** and validated with **Pydantic**.
  - Fully **Dockerized** (`Dockerfile` & `docker-compose.yml`) for seamless deployment.
  - Includes a **GitHub Actions CI/CD** pipeline for automated linting.
  - Deployed live to the cloud on Render.

---

## 🛠️ Tech Stack
*   **Data & ML:** Python, Pandas, Scikit-Learn (Random Forest, TF-IDF)
*   **Explainability & AI:** Groq API (Llama 3), Cosine Similarity (RAG)
*   **API & Frontend:** FastAPI, Uvicorn, Pydantic, HTML/TailwindCSS (ChatGPT-style UI)
*   **DevOps:** Docker, GitHub Actions, Render

---

## ⚙️ Quick Start (How to Run Locally)
To reproduce this environment locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eebbaasolomon3-max/insa-log-triage-capstone.git
   cd insa-log-triage-capstone
