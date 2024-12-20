from anime.routes import anime, users
from anime import app
from anime.models import create_db


@app.on_event("startup")
def on_startup():
    create_db()