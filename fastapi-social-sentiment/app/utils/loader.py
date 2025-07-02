import json
from datetime import datetime
from typing import List, Optional, Dict

def load_tweets(
    json_path: str = "tweets_dataset.json",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    limit: int = 10
) -> List[Dict]:
    """
    Carga y filtra tweets por fecha y cantidad desde un archivo JSON.

    Parámetros:
    - json_path: ruta al archivo JSON.
    - start_date, end_date: strings en formato YYYY-MM-DD.
    - limit: máximo número de tweets a devolver.

    Retorna:
    - Lista de tweets (dicts) filtrados.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        all_tweets = json.load(f)

    # Convertir fechas y filtrar
    def is_within_range(tweet):
        created_at = datetime.strptime(tweet["meta"]["created_at"], "%Y-%m-%d")
        if start_date:
            if created_at < datetime.strptime(start_date, "%Y-%m-%d"):
                return False
        if end_date:
            if created_at > datetime.strptime(end_date, "%Y-%m-%d"):
                return False
        return True

    filtered = list(filter(is_within_range, all_tweets))

    return filtered[:limit]
