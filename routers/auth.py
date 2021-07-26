from fastapi import APIRouter,Depends
from datetime import timedelta
from fastapi import HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from dependency import database,models,tk,hash

app = APIRouter(tags=["Auth"])
@app.post("/login")
def auth(rq:OAuth2PasswordRequestForm=Depends(),db:session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email==rq.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="email is not found")
    if not hash.verify(rq.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="password incorrect")
    access_token_expires = timedelta(minutes=tk.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = tk.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
