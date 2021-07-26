from fastapi import HTTPException,status
from dependency import models, hash


def create_U(rq,db):
    new_user = models.User(name=rq.name, email=rq.email,
                           password=hash.hashP(rq.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_u(id,db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    return user

def get_all(db):
    users = db.query(models.User).all()
    return users
