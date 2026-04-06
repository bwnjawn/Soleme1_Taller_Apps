from fastapi.testclient import TestClient
from main import app

# Creamos el cliente de pruebas vinculado a tu aplicación FastAPI
client = TestClient(app)

def test_get_time():
    """
    Prueba que el endpoint /time responda correctamente.
    """
    # Realiza una petición GET al endpoint solicitado [cite: 19]
    response = client.get("/time")
    
    # 1. Verifica que el código de estado sea 200 (OK)
    assert response.status_code == 200
    
    # 2. Verifica que la respuesta sea un formato JSON válido [cite: 19]
    data = response.json()
    assert "current_time" in data
    
    # 3. Verifica que el valor no esté vacío
    assert data["current_time"] is not None
