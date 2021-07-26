from typing import List
from fastapi import APIRouter,Depends
from sqlalchemy.orm import session
from dependency import schemas, database,oauth2
from rep import userd
router = APIRouter(prefix="/user",tags=["user"])
get_db = database.get_db

"""creating user """


@router.post("/", response_model=schemas.ShowUser)
def create_user(rq: schemas.User, db: session = Depends(get_db)):
    return userd.create_U(rq,db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id, db: session = Depends(get_db)):
    return userd.get_u(id,db)

@router.get("/",response_model=List[schemas.ShowUser])
def users_all(db: session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return userd.get_all(db)
