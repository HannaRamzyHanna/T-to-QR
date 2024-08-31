# test_app.py
import pytest
from app import app  # Import the Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Generate QR Code' in response.data

def test_qr_code_generation(client):
    response = client.post('/', data={'text': 'Hello'})
    assert response.status_code == 200
    assert b'QR Code' in response.data
