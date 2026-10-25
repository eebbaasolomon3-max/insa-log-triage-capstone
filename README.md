# INSA AI Engineering Capstone: Log Anomaly Detection & Alert Triage

**Student:** Eba Solomon
**Program:** INSA Summer Camp, 5th Batch (AI Engineering Track)

## Problem Statement
Security analysts face alert fatigue due to high volumes of system logs and a high false-positive rate in basic detectors. This project provides an end-to-end pipeline to detect anomalous log events, rank them by threat level, and provide a cited, RAG-based explanation for *why* an alert was flagged.

## Architecture
1. **Data Processing:** HDFS log data parsed and cleaned using Pandas.
2. **Machine Learning:** A Random Forest Classifier (via Scikit-Learn `Pipeline`) trained on TF-IDF text features and categorical features (`Level`, `Component`). Class imbalance handled via `class_weight='balanced'`.
3. **Explainability (RAG):** A lightweight retrieval system that matches triggered anomalies against a curated knowledge base of security rules using Cosine Similarity.
4. **Serving:** A FastAPI web server that exposes a `/predict` endpoint for real-time inference.

## Setup Instructions
To reproduce this environment locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/eebbaasolomon3-max/insa-log-triage-capstone.git
   cd insa-log-triage-capstone
