from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Character

router = APIRouter()

@router.get("/api/characters")
def get_all_characters(db: Session = Depends(get_db)):
    return db.query(Character).all()

@router.get("/api/characters/{char_id}")
def get_character(char_id: int, db: Session = Depends(get_db)):
    return db.query(Character).filter(Character.id == char_id).first()