from fastapi import FastAPI
from app.routers import emotion
from app.routers import tweets
from app.routers import stance


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

app.include_router(emotion.router, prefix="/emotion")
app.include_router(tweets.router, prefix="/tweets")
app.include_router(stance.router, prefix="/stance")