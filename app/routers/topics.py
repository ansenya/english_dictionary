from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import distinct
from app.models import Word
from app.routers.utils import get_page_for_topics
from app.schemas import PageModel
from app.dependencies import get_db

router = APIRouter()

@router.get(path="/topics/",
            response_model=PageModel[str],
            summary="Retrieve all distinct topics",
            tags=["Topics"])
def get_words(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(distinct(Word.topic))
    page = get_page_for_topics(query, page, limit)

    return page