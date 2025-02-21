from fastapi.testclient import TestClient
from app import app

client = TestClient(app)  

def test_successful_prediction():
    response = client.post("/predict", json={"ticker": "AAPL"})
    
    assert response.status_code == 200
    data = response.json()

    assert "ticker" in data
    assert data["ticker"] == "AAPL"
    assert "forecast" in data
    assert isinstance(data["forecast"], list)
    assert len(data["forecast"]) > 0
    assert all("yhat" in item for item in data["forecast"])  # Check key existence

def test_invalid_input():
    response = client.post("/predict", json={})  # Missing ticker
    assert response.status_code == 422  # Unprocessable Entity

def test_model_not_found():
    response = client.post("/predict", json={"ticker": "INVALID_TICKER"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Model not found."
