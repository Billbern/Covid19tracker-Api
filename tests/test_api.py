import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client):
    """Test that the index route returns 200 and some data or 404 with error msg."""
    response = client.get('/api/v1/')
    assert response.status_code in [200, 404]
    data = response.get_json()
    assert "status" in data

def test_invalid_date_route(client):
    """Test with an invalid date string."""
    response = client.get('/api/v1/invalid-date')
    assert response.status_code == 404
    data = response.get_json()
    assert data["status"] == "error"
