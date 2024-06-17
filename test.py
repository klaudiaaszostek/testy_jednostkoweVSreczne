import pytest
from flask import Flask, jsonify, request
from app import app, users

@pytest.fixture
def client():
    app.config['TESTING'] = True
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
    assert data['error'] == 'Invalid data'

def test_create_user_no_name(client):
    # W aktualnej implementacji aplikacji, formularz wymaga pola "name", 
    # więc test ten jest trudny do wykonania ręcznie bez modyfikacji kodu.
    # W automatycznych testach, to jest sprawdzane bezpośrednio poprzez 
    # przesyłanie błędnego JSONa do endpointu /user.
    response = client.post('/user', json={'age': 25})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == 'Invalid data'

def test_user_added_to_list(client):
    users.clear()  # Clear users list before test
    response = client.post('/user', json={'name': 'Alice'})
    assert response.status_code == 201
    assert len(users) == 1
    assert users[0]['name'] == 'Alice'

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask App!' in response.data


    