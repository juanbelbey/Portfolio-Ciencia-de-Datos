from fastapi import APIRouter, Query
from typing import Optional
from app.utils.loader import load_tweets
from app.services.classifier import predict_stance
from app.services.elastic import es
from elastic_transport import ConnectionTimeout


router = APIRouter()

@router.get("/")

def detect_stance(
    limit: int = 10,
    start_date: Optional[str] = Query(None),
    end_date: Optional[str] = Query(None)
):
    tweets = load_tweets(start_date=start_date, end_date=end_date, limit=limit)

    resultados = []
    for tweet in tweets:
        texto = tweet["payload"]["tweet"]["content"]
        stance = predict_stance(texto)

        try:
            es.update(index="tweets", id=tweet["id"], body={
                "doc": {"stance": stance}
            })
        except ConnectionTimeout:
            return {
                "error": "No se pudo conectar a Elasticsearch. Por favor, asegurate de que el contenedor esté corriendo.",
                "detalle": f"Tweet {tweet['id']} no fue actualizado."
            }

        resultados.append({
            "id": tweet["id"],
            "texto": texto,
            "stance": stance
        })

    return {"cantidad": len(resultados), "resultados": resultados}
