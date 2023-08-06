from fastapi.testclient import TestClient
from app.trifledb_server import app

client = TestClient(app)

def test_read_main_v1():
    response = client.get("/v1/blah")
    assert response.status_code == 200
    assert response.json() == {"key not found"}
