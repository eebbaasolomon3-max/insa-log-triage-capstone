from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import joblib
import pandas as pd
import os
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq
from dotenv import load_dotenv

# Load environment variables (API Key)
load_dotenv()

app = FastAPI(title="INSA SOC Copilot API")

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Load Model
MODEL_PATH = "models/baseline_rf_pipeline.pkl"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    raise RuntimeError(f"Model not found at {MODEL_PATH}")

class LogEntry(BaseModel):
    component: str
    level: str
    event_template: str

class ChatMessage(BaseModel):
    message: str
    log_context: str
    history: list = []

# MITRE ATT&CK Mapping
MITRE_MAPPING = {
    "dfs.DataNode": "T1499 - Endpoint Denial of Service",
    "dfs.FSNamesystem": "T1565 - Data Manipulation",
    "dfs.DataBlockScanner": "T1485 - Data Destruction",
    "default": "T1078 - Valid Accounts (Unusual Behavior)"
}

knowledge_base = [
    "Rule 1: High volume of 'DataNode' terminated signals indicates network disconnection or hardware failure.",
    "Rule 2: 'WARN' in 'dfs.FSNamesystem' points to a corrupted block or NameNode failure.",
    "Rule 3: Repeated 'BLOCK* NameSystem.addStoredBlock' is a potential denial-of-service attack."
]

def get_rag_context(log_template, log_component):
    query = f"{log_component} {log_template}"
    vectorizer = TfidfVectorizer(stop_words='english')
    kb_vectors = vectorizer.fit_transform(knowledge_base)
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, kb_vectors)[0]
    best_idx = similarities.argmax()
    return knowledge_base[best_idx] if similarities[best_idx] > 0.1 else "No specific rule matched."

# --- FRONTEND ---
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("app/static/index.html")

# --- PREDICT ENDPOINT (Single Log) ---
@app.post("/predict")
def predict_anomaly(log: LogEntry):
    try:
        input_df = pd.DataFrame([{'EventTemplate': log.event_template, 'Level': log.level, 'Component': log.component}])
        prediction = model.predict(input_df)[0]
        
        if log.level == "ERROR":
            prediction = "Anomaly"

        response = {"prediction": prediction, "explanation": "Normal behavior detected.", "mitre_tactic": "N/A"}
        
        if prediction == 'Anomaly':
            rag_rule = get_rag_context(log.event_template, log.component)
            mitre = MITRE_MAPPING.get(log.component, MITRE_MAPPING["default"])
            
            prompt = f"You are a Cybersecurity Analyst. Anomaly detected in {log.component}. Log: {log.event_template}. Rule: {rag_rule}. MITRE: {mitre}. Provide a brief 2-sentence incident report."
            
            try:
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="openai/gpt-oss-20b",
                )
                explanation = chat_completion.choices[0].message.content
            except Exception as e:
                explanation = f"Static Rule: {rag_rule} (LLM Error: {str(e)})"
                
            response["explanation"] = explanation
            response["mitre_tactic"] = mitre
            
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- BATCH UPLOAD ENDPOINT (CSV) ---
@app.post("/upload")
async def upload_logs(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        # Check for required columns
        required_cols = ['EventTemplate', 'Level', 'Component']
        if not all(col in df.columns for col in required_cols):
            raise HTTPException(status_code=400, detail="CSV must contain EventTemplate, Level, and Component columns.")
        
        # Run predictions on all rows
        predictions = model.predict(df[required_cols])
        
        # Count anomalies
        df['Prediction'] = predictions
        anomalies = df[df['Prediction'] == 'Anomaly']
        
        total_logs = len(df)
        total_anomalies = len(anomalies)
        
        # Get top 5 anomalies for the UI
        top_alerts = anomalies.head(5).to_dict(orient='records')
        
        return {
            "total_logs": total_logs,
            "total_anomalies": total_anomalies,
            "top_alerts": top_alerts
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- CHAT COPILOT ENDPOINT ---
@app.post("/chat")
def chat_with_analyst(msg: ChatMessage):
    try:
        messages = [
            {"role": "system", "content": f"You are an expert Cybersecurity Copilot for INSA. Log context: '{msg.log_context}'. Answer professionally. Use bullet points for lists."}
        ]
        for chat in msg.history:
            messages.append({"role": chat["role"], "content": chat["content"]})
        messages.append({"role": "user", "content": msg.message})

        chat_completion = client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-20b",
        )
        return {"reply": chat_completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
