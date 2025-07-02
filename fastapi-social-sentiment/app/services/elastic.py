from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from elastic_transport import ConnectionError

# Conexión local
es = Elasticsearch("http://localhost:9200")



es = Elasticsearch("http://localhost:9200")

def ensure_index(index_name="tweets"):
    try:
        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name, body={
                "mappings": {
                    "properties": {
                        "id": {"type": "integer"},
                        "texto": {"type": "text"},
                        "emocion": {"type": "keyword"},
                        "score": {"type": "float"},
                        "created_at": {"type": "date"},
                        "stance": {"type": "keyword"}
                    }
                }
            })
    except ConnectionError:
        print(f"[!] No se pudo conectar a Elasticsearch para verificar o crear el índice '{index_name}'.")


def upsert_tweet(tweet_id: int, doc: dict, index_name="tweets"):
    """
    Guarda o actualiza un tweet en el índice por ID.
    """
    es.index(index=index_name, id=tweet_id, document=doc)