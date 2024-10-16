from fastapi import FastAPI
from config import engine, Base
from app.routers import words, topics

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(words.router)
app.include_router(topics.router)
