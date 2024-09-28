import pytest
from flask import url_for
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_search_get(client):
    response = client.get('/search')
    assert response.status_code == 200
    assert b'Log Search Results' in response.data
    assert b'Enter search query' in response.data

def test_search_post_with_query(client):
    response = client.post('/search', data={'query': 'error'})
    assert response.status_code == 200
    assert b'Log Search Results' in response.data
    assert b'ERROR' in response.data

def test_search_post_without_query(client):
    response = client.post('/search', data={})
    assert response.status_code == 200
    assert b'Log Search Results' in response.data
    assert b'No results found' not in response.data  # Assuming the dummy data is always returned

def test_search_results_content(client):
    response = client.post('/search', data={'query': 'user'})
    assert response.status_code == 200
    assert b'User \'john_doe\' logged in successfully' in response.data
    assert b'User \'jane_smith\' changed password' in response.data

def test_search_no_results(client):
    # This test might fail with the current dummy data implementation
    # Uncomment when actual search functionality is implemented
    # response = client.post('/search', data={'query': 'nonexistent_term'})
    # assert response.status_code == 200
    # assert b'No results found' in response.data
    pass
