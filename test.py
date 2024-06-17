import pytest
from app import app, users

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_user_success(client):
    response = client.post('/user', json={'name': 'Alice'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Alice'
    assert 'id' in data

def test_create_user_no_data(client):
    response = client.post('/user', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_create_user_no_name_field(client):
    response = client.post('/user', json={'age': 25})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_user_added_to_list(client):
    users.clear()  # Wyczyść listę użytkowników przed testem
    response = client.post('/user', json={'name': 'Alice'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Alice'
    assert len(users) == 1
    assert users[0]['name'] == 'Alice'

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Create User' in response.data

if __name__ == '__main__':
    pytest.main()
