from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_time():

    response = client.get('/time')
    assert response.status_code == 200
    assert 'hora_actual' in response.json()


def test_not_found():
    response = client.get('/invalid-route')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
