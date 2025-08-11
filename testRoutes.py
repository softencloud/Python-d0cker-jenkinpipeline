import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Jenkins Tutorials" in response.data

