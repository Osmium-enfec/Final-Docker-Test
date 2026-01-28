import pytest
from django.test import Client

@pytest.fixture
def client():
    return Client()

def test_greet_with_name(client):
    response = client.get('/?name=Alice')
    assert response.status_code == 200
    assert response.json() == {'greeting': 'Hello, Alice!'}

def test_greet_without_name(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'greeting': 'Hello, World!'}
