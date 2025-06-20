from fastapi import FastAPI, HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session 

app=FastAPI()
models.Base.metadata.create_all(bind=engine)

class PostBase(BaseModel):
    title:str
    content:str
    user_id:int

class UserBase(BaseModel):
    username:str

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@app.post("/users/",status_code=status.HTTP_201_CREATED)
async def create_user(user:UserBase,db:db_dependency):
    db_user=models.User(**user.dict())
    db.add(db_user)
    db.commit()
     
@app.get("/users/{user_id}",status_code=status.HTTP_200_OK)
async def read_user(user_id:int,db:db_dependency):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found!")
    return user
@app.post("/posts/",status_code=status.HTTP_201_CREATED)
async def crate_post(post:PostBase,db:db_dependency):
    db_post=models.Post(**post.dict())
    db.add(db_post)
    db.commit()
@app.get("/all-posts",status_code=status.HTTP_200_OK)
async def get_all_post(db:db_dependency):
    posts=db.query(models.Post).all()
    if posts is None:
        raise HTTPException(
            status_code=404,
            detail="no post found in the database"
            )
    return posts