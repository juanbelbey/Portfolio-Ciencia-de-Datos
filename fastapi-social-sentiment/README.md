# FastAPI Social Sentiment

**Autor:** Juan Belbey

---
## 📝 Introducción

Este proyecto implementa una API en **FastAPI** para analizar el sentimiento y la postura política en tweets. Se extraen datos de un archivo JSON, se aplican **modelos de NLP** para clasificar emociones y postura, y los resultados se almacenan en **Elasticsearch**, facilitando su consulta y análisis.

A partir de esta base, es posible generar dashboards de sentimiento, alertas tempranas en redes sociales y alimentar pipelines de monitoreo de opinión pública en tiempo real.


## 🎯 Objetivos

1. **Construir** un pipeline ETL para extraer tweets, aplicar modelos de NLP y cargarlos en Elasticsearch.
2. **Demostrar** la integración de FastAPI con **Transformers** de Hugging Face y LLMs (local y remoto).
3. **Exponer** endpoints REST para:
   - Clasificar emociones de tweets.
   - Detectar postura (SUPPORT / OPPOSE / NEUTRAL).
   - Consultar resultados con paginación y filtros de fecha.
4. **Soporte en producción**: servir como base para dashboards de sentimiento, alertas tempranas basadas en emociones y estudios de evolución de la opinión pública.

---

## 🌐 Descripción general

1. **Extracción**

   - **Origen actual**: lectura de `tweets_dataset.json`.
   - **Extensible**: conectar APIs como Twitter/X con [`tweepy`](https://www.tweepy.org/) o REST para ingestar datos en tiempo real.

2. **Transformación**

   - **Emoción**: `j-hartmann/emotion-english-distilroberta-base` (DistilRoBERTa, optimizado para 7 emociones básicas).
   - **Postura (stance)**:
     - **Local**: zero-shot con `facebook/bart-large-mnli` (modelo NLI de alto rendimiento sin fine-tuning).
     - **Remoto (opcional)**: Groq API con `llama-3.3-70b-versatile` (LLM versátil y eficiente para clasificación).

3. **Carga**

   - Inserción/upsert en índice `tweets` de **Elasticsearch 8.x**.

---

## 🐳 Levantar todo con Docker Compose

Trabajamos con **Docker Compose** para levantar Elasticsearch y la API de manera conjunta:

```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.8.1
    container_name: es-tweets
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
      - "9300:9300"
    healthcheck:
      test: ["CMD-SHELL", "curl -s http://localhost:9200 || exit 1"]
      interval: 10s
      retries: 5

  api:
    build: .
    container_name: tweets-api
    depends_on:
      elasticsearch:
        condition: service_healthy
    ports:
      - "8000:8000"
    environment:
      - STANCE_MODE=${STANCE_MODE}
      - GROQ_API_KEY=${GROQ_API_KEY}
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Arranca todo con:
```bash
docker-compose up --build
```

---

## 🛡️ Manejo de errores

- Tratamiento de `ConnectionTimeout` con Elasticsearch para evitar caídas.
- Fallbacks y mensajes claros si APIs externas no responden.
- Procesamiento individual de tweets para manejo robusto.

---

## 🔍 Endpoints

| Ruta       | Método | Descripción                                       |
| ---------- | ------ | ------------------------------------------------- |
| `/emotion` | GET    | Clasifica emociones y guarda en Elasticsearch     |
| `/stance`  | GET    | Detecta postura y guarda en Elasticsearch         |
| `/tweets`  | GET    | Recupera tweets procesados (paginación y filtros) |

**Parámetros comunes:**

- `limit` (int) – Máximo de tweets a procesar o devolver.
- `offset` (int) – Paginación (`/tweets`).
- `start_date`, `end_date` (YYYY-MM-DD) – Filtros por rango de fechas.

---

## 📚 Modelos usados

- **Emoción**:
  - `j-hartmann/emotion-english-distilroberta-base` – DistilRoBERTa entrenado para 7 emociones: anger, disgust, fear, joy, sadness, surprise, neutral.

- **Postura (stance):**
  - **Local**: `facebook/bart-large-mnli` – NLI zero-shot rápido y offline.
  - **Remoto**: `llama-3.3-70b-versatile` (via Groq API) – LLM de alta capacidad para clasificación precisa.

---

## ⚙️ Requisitos

- **Python** 3.11
- **Docker** y **Docker Compose**
- **Elasticsearch** 8.x
- **GROQ_API_KEY** (opcional)

---

## 🛠 Arquitectura

```
fastapi-tweets-etl/
├── app/
│   ├── routers/
│   │   ├── emotion.py
│   │   ├── stance.py
│   │   └── tweets.py
│   ├── services/
│   │   ├── classifier.py
│   │   └── elastic.py
│   └── utils/
│       └── loader.py
├── main.py
├── tweets_dataset.json
├── requirements.txt
├── .env.example
├── docker-compose.yml
├── LICENSE.md
└── README.md
```

---

## 🚀 Integración

Esta API está lista para integrarse a un entorno mayor de procesamiento y monitorización de opinión pública.

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**. Consulta el archivo [LICENSE.md](LICENSE.md) para más detalles.

