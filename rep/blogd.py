from sqlalchemy.orm import session
from fastapi import HTTPException,status
from dependency import models
def get_all(db):
    blogs = db.query(models.Blog).all()
    return blogs
def create_blog(db,request):
    new_blog = models.Blog(title=request.title,
                           body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog  # after using response_model only clean return not use {} return
def delete(id,db):
     blog = db.query(models.Blog).filter(models.Blog.id == id)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="blog with id {id} not found")
     blog.delete(synchronize_session=False)
     db.commit()

     return {"result": f"the id {id} of blog deleted"}
def update(id,db,request):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found")

    blog.title = request.title
    blog.user_id = request.user_id
    blog.body = request.body
    db.commit()
    db.refresh(blog)
    return blog
def get_id(id,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"the blog with {id} not found !")
    return blog
