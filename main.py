from fastapi import FastAPI
from config import engine, Base
from app.routers import words, topics


app = FastAPI(
    title="English Dictionary API",
    description="API for managing an English dictionary.",
    version="0.0.1"
)

Base.metadata.create_all(bind=engine)

app.include_router(words.router)
app.include_router(topics.router)
