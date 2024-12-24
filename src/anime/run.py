from anime import app
from anime.models import create_db_and_tables


@app.on_event("startup")
def on_startup():
    create_db_and_tables()