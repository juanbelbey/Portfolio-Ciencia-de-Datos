# app/routers/tweets.py

from fastapi import APIRouter, Query
from typing import Optional
from app.services.elastic import es

router = APIRouter()

@router.get("/")
def get_tweets(
    limit: int = Query(10, ge=1),              # ya no tiene 'le=100'
    offset: int = Query(0, ge=0),
    start_date: Optional[str] = Query(None, description="Formato YYYY-MM-DD"),
    end_date:   Optional[str] = Query(None, description="Formato YYYY-MM-DD"),
):
    must_filters = []
    if start_date or end_date:
        date_range = {}
        if start_date:
            date_range["gte"] = start_date
        if end_date:
            date_range["lte"] = end_date
        must_filters.append({"range": {"created_at": date_range}})

    query = {
        "from": offset,
        "size": limit,
        "query": {
            "bool": {
                "must": must_filters
            }
        }
    }

    response = es.search(index="tweets", body=query)

    resultados = []
    for hit in response["hits"]["hits"]:
        doc = hit["_source"]
        doc["id"] = hit["_id"]
        resultados.append(doc)

    return {"cantidad": len(resultados), "resultados": resultados}
