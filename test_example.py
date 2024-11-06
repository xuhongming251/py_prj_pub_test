# test_example.py
import requests

def test_health_check():
    response = requests.get('http://localhost:8080/api/health')
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
