from fastapi import FastAPI
from dependency import database, models
from routers import blogs, users, auth

tags_metadata = [
    {
        "name": "Auth",
        "description": "**for authentication**"
    },
    {
        "name": "user",
        "description": "Operations with users. The **login** logic _is_ also here.",
    },
    {
        "name": "blogs",
        "description": "Manage all blogs related info.",
        # "externalDocs": {
        #     "description": "Items external docs",
        #     "url": "https://fastapi.tiangolo.com/",
        # },
    },
]
app = FastAPI(title="BLOGS API", description="**Tesing with youtube videos tutorial**",
              version="1.0.0.x", openapi_tags=tags_metadata)

models.Base.metadata.create_all(database.engine)  # to create table in database
app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(auth.app)


@app.get("/", tags=['index'])  # index path
def index():
    return {"result": "helloworld"}
