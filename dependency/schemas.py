"""this is to show in docs and some validation purpose in fastapi"""
# thats's why we we use request:Blog in adding data


from pydantic import BaseModel
from typing import Optional,List


class Blog(BaseModel):

    title: Optional[str]
    body: Optional[str]
    user_id: int

    class Config:
        orm_mode = True


class User(BaseModel):

    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


""" below schemas is used to hide some info like passwords and sensitive info to other users """#starts with Show





class ShowUser(BaseModel):
    name: str
    email: str
    owner:List[Blog]=[]

    class Config:
        orm_mode = True




class ShowBlog(BaseModel):
    title: Optional[str]
    body: Optional[str]
    creator: ShowUser

    class Config:  # to know more goto pydantic docs and in orm_mode docs
        orm_mode = True


class UserVerify(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
