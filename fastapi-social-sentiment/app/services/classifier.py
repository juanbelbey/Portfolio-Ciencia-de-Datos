import os
import requests
from dotenv import load_dotenv, find_dotenv
from transformers import pipeline

# Cargar .env de forma explícita y override
dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)

# Carga variables de entorno (archivo .env sin comentarios)
load_dotenv()

# STANCE_MODE limpio y en minúsculas
STANCE_MODE = os.getenv("STANCE_MODE", "local").strip().lower()

# Tokens para APIs externas
GROQ_TOKEN = os.getenv("GROQ_API_KEY", "").strip()

# Modelo de emociones (siempre lo cargamos)
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def predict_emotion(text: str):
    out = emotion_model(text)
    # Si out[0] es lista, extraemos el dict; si no, out[0] ya es dict
    first = out[0][0] if isinstance(out[0], list) else out[0]
    return {"label": first["label"], "score": round(first["score"], 4)}


# Preparar la variable para carga perezosa del modelo local de stance
stance_model_local = None

def predict_stance(text: str) -> str:
    """Detecta SUPPORT, OPPOSE o NEUTRAL según STANCE_MODE."""
    global stance_model_local

    # --- MODELO LOCAL (zero-shot) ---
    if STANCE_MODE == "local":
        if stance_model_local is None:
            stance_model_local = pipeline(
                "zero-shot-classification",
                model="facebook/bart-large-mnli"
            )
        labels = ["SUPPORT", "OPPOSE", "NEUTRAL"]
        result = stance_model_local(text, candidate_labels=labels)
        return result["labels"][0] if result.get("labels") else "NEUTRAL"

    # --- GROQ LLM API ---
    if STANCE_MODE == "groq" and GROQ_TOKEN:
        prompt = (
            f'You are a political analyst. Read the following tweet and classify the author\'s opinion as SUPPORT, OPPOSE, or NEUTRAL.\n'
            f'Tweet: "{text}"\n'
            'Answer:'
        )
        headers = {"Authorization": f"Bearer {GROQ_TOKEN}", "Content-Type": "application/json"}
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
            "max_tokens": 10,
            "top_p": 1
        }
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )
        data = response.json()
        content = data["choices"][0]["message"]["content"].strip().upper()
        for option in ["SUPPORT", "OPPOSE", "NEUTRAL"]:
            if option in content:
                return option

    # --- Fallback por defecto ---
    return "NEUTRAL"
