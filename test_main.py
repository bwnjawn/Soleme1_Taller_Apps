from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_time():

    response = client.get('/time')
    assert response.status_code == 200
    assert 'current_time' in response.json()
    
def test_not_found():
    """
    Verifica que la API maneje correctamente rutas que no existen.
    """
    response = client.get("/invalid-route")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
