from fastapi import APIRouter, HTTPException , status
from app.models.Users import Users
from sqlmodel import Session, select

router = APIRouter(prefix="/Users", tags=["Users"])
from ..database import engine

@router.get("/", summary="Get all Users")
async def get_all():
    with Session(engine) as session:
        statement = select(Users)
        results = session.exec(statement).all()
        return results



@router.post("/", summary="Create a new Users", status_code=status.HTTP_201_CREATED)
async def create_item(_Users : Users):
    with Session(engine) as session:
        session.add(_Users)
        session.commit()
        session.refresh(_Users)
        return _Users


@router.get("/{item_id}", summary="Get Users by ID")
async def get_item(item_id: int):
    with Session(engine) as session:
        item = session.get(Users, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users not found")
        return item



@router.put("/{item_id}", summary="Update Users")
async def update_item(_Users : Users , item_id: int):
    with Session(engine) as session:

        item = session.get(Users, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users not found")

        for key, value in _Users.model_dump(exclude_unset=True).items():
            setattr(item, key, value)

        session.add(item)
        session.commit()
        session.refresh(item)
        return item


@router.delete("/{item_id}", summary="Delete Users" ,status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):

    with Session(engine) as session:
        item = session.get(Users, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Users not found")

        session.delete(item)
        session.commit()
        return None
