from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Word
from app.routers.utils import get_page
from app.schemas import WordOut, PageModel
from app.dependencies import get_db

router = APIRouter()

@router.get(path="/words/",
            response_model=PageModel[WordOut],
            summary="Retrieve all distinct words and their translation",
            tags=["Words"])
def get_words(page: int = 1, limit: int = 10, topic: str = None, db: Session = Depends(get_db)):
    query = db.query(Word)
    if topic:
        query = query.filter_by(topic=topic)
    page = get_page(query, page, limit)

    return page