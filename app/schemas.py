from typing import Generic, List, TypeVar

from pydantic import BaseModel

T = TypeVar("T")

class WordCreate(BaseModel):
    word: str
    translation: str
    topic: str

class WordOut(WordCreate):
    id: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username: str
    password: str

class TopicOut(BaseModel):
    topic: str

class PageModel(BaseModel, Generic[T]):
    items: List[T]
    limit: int
    total_pages: int
    current_page: int

