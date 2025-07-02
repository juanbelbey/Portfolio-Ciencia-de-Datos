from fastapi import APIRouter, Query
from typing import Optional
from app.utils.loader import load_tweets
from app.services.classifier import predict_emotion
from app.services.elastic import ensure_index, upsert_tweet

router = APIRouter()

# Asegurar que el índice exista antes de usarlo
ensure_index()

@router.get("/")
def process_emotions(
    limit: int = 10,
    start_date: Optional[str] = Query(None, description="Formato YYYY-MM-DD"),
    end_date: Optional[str] = Query(None, description="Formato YYYY-MM-DD")
):
    tweets = load_tweets(start_date=start_date, end_date=end_date, limit=limit)

    resultados = []
    for tweet in tweets:
        texto = tweet["payload"]["tweet"]["content"]
        emocion = predict_emotion(texto)

        doc = {
            "id": tweet["id"],
            "texto": texto,
            "emocion": emocion["label"],
            "score": emocion["score"],
            "created_at": tweet["meta"]["created_at"]
        }

        upsert_tweet(tweet_id=tweet["id"], doc=doc)
        resultados.append(doc)

    return {"cantidad": len(resultados), "resultados": resultados}
