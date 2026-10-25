## 🌐 Live Demo
👉 **[Click here to test the Live Interactive Dashboard](https://insa-log-triage-capstone.onrender.com)** 👈

# 🛡️ INSA AI Engineering Capstone: Log Anomaly Detection & Alert Triage
**Student:** Eba Solomon | **Program:** INSA Summer Camp, 5th Batch

An end-to-end MLOps pipeline that detects anomalies in HDFS system logs and uses Retrieval-Augmented Generation (RAG) to explain *why* an alert was triggered, reducing analyst alert fatigue.

## 🚀 What I Built (Key Achievements)
- **Exploratory Data Analysis (EDA):** Cleaned and parsed raw HDFS logs, discovering a massive class imbalance (only 2% anomalies) that breaks standard accuracy metrics.
- **Machine Learning Pipeline:** Built a leak-proof `scikit-learn` pipeline using TF-IDF for text log templates and One-Hot Encoding for categorical features. Trained a `RandomForestClassifier` using `class_weight='balanced'` to prioritize catching rare anomalies.
- **RAG Explainability Layer:** Implemented a lightweight semantic search using `Cosine Similarity` to match flagged anomalies against a curated security knowledge base, returning human-readable explanations with confidence scores.
- **MLOps & Serving:** Deployed the trained model as a production-ready web API using **FastAPI** and **Uvicorn**, complete with Pydantic input validation to prevent malformed data attacks.
- **Security & Documentation:** Added a strict `.gitignore` to prevent raw data leaks, and documented a formal Model Card detailing limitations and ethical use.

## 🛠️ Tech Stack
*   **Data & ML:** Python, Pandas, Scikit-Learn (Random Forest, TF-IDF)
*   **API & Deployment:** FastAPI, Uvicorn, Pydantic
*   **Environment:** Jupyter Notebook, Git

## ⚙️ Quick Start (How to Run)
To reproduce this environment locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eebbaasolomon3-max/insa-log-triage-capstone.git
   cd insa-log-triage-capstone
