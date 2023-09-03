import pytest
from flask import url_for
from app.backend.factory import create_app


@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
    })

    with app.app_context():
        yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_page(client):
    response = client.get(url_for('home'))
    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_login_page(client):
    response = client.get(url_for('login'))
    assert response.status_code == 200
    assert b"Login" in response.data


def test_register_page(client):
    response = client.get(url_for('register'))
    assert response.status_code == 200
    assert b"Register" in response.data
