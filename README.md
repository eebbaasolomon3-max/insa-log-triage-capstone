kk# 🛡️ INSA AI Engineering Capstone: Log Anomaly Detection & Threat Intelligence Copilot

**Student:** Eba Solomon | **Program:** INSA Summer Camp, 5th Batch (AI Engineering Track)

## 🌐 Live Interactive Demo
👉 **[Click here to test the Live SOC Dashboard](https://insa-log-triage-capstone.onrender.com)** 👈
*(Note: Hosted on Render's free tier. If the server is asleep, the first load may take 30–50 seconds).*

---

## 📌 Executive Summary
Security Operations Centers (SOCs) face severe **alert fatigue** due to high volumes of system logs and a high false-positive rate in basic detectors. Furthermore, modern AI models are often "black boxes"—when they flag an anomaly, analysts don't know *why*.

This project is a **full-stack, production-ready AI platform** that ingests HDFS system logs, detects anomalies using dual-model AI, maps threats to the MITRE ATT&CK framework, and uses a Large Language Model (Llama 3) to generate dynamic incident reports and provide an interactive mitigation chat.

---

## 🚀 Core Capabilities & Features Built

### 1. Dual-Model Machine Learning (Supervised + Unsupervised)
*   **Supervised AI (Random Forest):** Trained on TF-IDF text features and One-Hot Encoded categorical features. Uses `class_weight='balanced'` to heavily penalize false negatives, ensuring known threats are caught.
*   **Unsupervised AI (Isolation Forest):** Deployed alongside the RF model to detect **Zero-Day threats**. It isolates anomalies based on structural deviations without needing ground-truth labels.
*   **Batch Processing:** Handles high-volume log analysis via a Drag-and-Drop CSV upload, complete with a real-time Doughnut Chart visualization of the Normal vs. Anomaly ratio.

### 2. Generative AI & RAG (Retrieval-Augmented Generation)
*   **LLM Incident Reports:** When an anomaly is detected, a Llama-3 model generates a professional 2-sentence incident report based on the specific log context.
*   **Stateful SOC Copilot Chat:** A custom ChatGPT-style interface where analysts can ask follow-up questions (e.g., *"How do I mitigate this?"*). The backend retains conversation history for contextual awareness.
*   **Markdown Rendering:** The frontend uses `marked.js` to render LLM responses with perfect formatting, bolding, and bullet points.

### 3. Cybersecurity & Trustworthy AI
*   **MITRE ATT&CK Mapping:** Automatically classifies detections into tactics like `T1565 - Data Manipulation` or `T1499 - Denial of Service`.
*   **Prompt Injection Defense:** Includes a built-in defense test demonstrating the AI's ability to reject jailbreak attempts and malicious instructions.
*   **Pydantic Validation:** Strict input validation on the FastAPI backend prevents malformed data attacks.

### 4. MLOps & Cloud Architecture
*   **FastAPI Backend:** High-performance, asynchronous API serving both the ML models and the LLM endpoints.
*   **Dockerized:** Fully containerized with `Dockerfile` and `docker-compose.yml` for reproducible deployments.
*   **CI/CD Pipeline:** Includes a GitHub Actions workflow for automated Python linting and syntax checking on every push.
*   **Cloud Deployment:** Live on Render.

---

## 🎓 INSA Curriculum Alignment (M01 - M18)

This project was deliberately engineered to integrate and demonstrate every module in the INSA AI Engineering syllabus:

| Module | Topic | Implementation in Project |
| :--- | :--- | :--- |
| **M01-M02** | Toolchain & Python | Git structure, `.gitignore` security, Python OOP. |
| **M03** | Mathematics | Vectorization, Cosine Similarity for RAG, Class imbalance math. |
| **M04-M05** | Data Wrangling & EDA | HDFS log parsing, handling text templates, EDA charts. |
| **M06-M09** | Supervised ML | Scikit-Learn Pipeline, TF-IDF, Random Forest, Stratified Splits. |
| **M10** | Unsupervised ML | Isolation Forest for zero-day anomaly detection. |
| **M14-M15** | LLMs & RAG | Groq API, Llama-3, stateful chat memory, semantic search. |
| **M16** | MLOps | FastAPI, Docker, GitHub Actions, Render deployment, Joblib. |
| **M17-M18** | Trustworthy AI & Capstone | MITRE mapping, Prompt Injection defense, Model Card, UI/UX. |

---

## 🛠️ Tech Stack
*   **Data & ML:** Python, Pandas, Scikit-Learn (Random Forest, Isolation Forest, TF-IDF)
*   **Explainability & AI:** Groq API (Llama 3), Cosine Similarity (RAG)
*   **API & Frontend:** FastAPI, Uvicorn, Pydantic, HTML/TailwindCSS, Chart.js, Marked.js
*   **DevOps:** Docker, GitHub Actions, Render

---

## ⚙️ Local Setup & Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/eebbaasolomon3-max/insa-log-triage-capstone.git
   cd insa-log-triage-capstone
