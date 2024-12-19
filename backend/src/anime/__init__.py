from fastapi import FastAPI
from anime.routes import users, anime

app = FastAPI()

app.include_router(anime.router)
app.include_router(users.router)