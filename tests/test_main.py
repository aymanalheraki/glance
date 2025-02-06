from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_shorten_url():
    response = client.post("/shorten", json={"long_url": "https://example.com"})
    assert response.status_code == 200
    assert "short_url" in response.json()

def test_redirect_url():
    response = client.post("/shorten", json={"long_url": "https://example.com"})
    short_url = response.json()["short_url"]
    short_code = short_url.split("/")[-1]

    response = client.get(f"/{short_code}")
    assert response.status_code == 302
