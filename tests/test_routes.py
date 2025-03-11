import pytest
from flask import Flask
from src.api.routes import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_register(client):
    response = client.post('/register', json={'user': 'test_user'})
    assert response.status_code == 201
    assert response.json == {"message": "User registered successfully"}

def test_submit_knowledge(client):
    client.post('/register', json={'user': 'test_user'})
    response = client.post('/submit_knowledge', json={'user': 'test_user', 'knowledge': 'test_knowledge', 'proof': 'test_proof'})
    assert response.status_code == 201 or response.status_code == 400

def test_balance(client):
    client.post('/register', json={'user': 'test_user'})
    response = client.get('/balance', query_string={'user': 'test_user'})
    assert response.status_code == 200
    assert 'balance' in response.json
