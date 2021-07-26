from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import session
from dependency import schemas,database,oauth2
from rep import blogd
get_db = database.get_db

router = APIRouter(prefix="/blog",tags=["blogs"])


# getting all blog data
@router.get("/data", response_model=List[schemas.ShowBlog])
def get_all_blogs(db:session = Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blogd.get_all(db)
    


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowBlog)
def create_blog(request: schemas.Blog, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # Blog is refrence to schemas to docs
    return blogd.create_blog(db,request)


# get blog by id
@router.get("/{id}", response_model=schemas.ShowBlog)
def bolg_id(id: int, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogd.get_id(id,db)


@router.delete("/{id}")  # deleting the blog with id
def delete_it(id: int, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogd.delete(id,db)


@router.put("/{id}")  # updating the blog with id
def update_blog(id, request: schemas.Blog, db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogd.update(id,db,request)
