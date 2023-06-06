from fastapi import FastAPI
from routes import get_method, post_method


app = FastAPI()
app.include_router(get_method.router)
app.include_router(post_method.router)
