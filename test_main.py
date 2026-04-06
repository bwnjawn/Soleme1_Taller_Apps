from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_time():
    # TestClient usa httpx internamente para esta llamada
    response = client.get('/time')
    assert response.status_code == 200
    assert 'current_time' in response.json()
