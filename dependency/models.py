from sqlalchemy import Column,String,Integer,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__="blogs"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer,ForeignKey('users.id'))#foreinkey is tablename.id
    creator = relationship("User",back_populates="owner")

class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    owner = relationship("Blog",back_populates="creator")