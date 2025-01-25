from fastapi.testclient import TestClient
from anime import app


client = TestClient(app)