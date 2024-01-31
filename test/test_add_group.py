# Generated by Selenium IDE
from model.group import Group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_addgroup(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "bzz is perfect",header = "sasdasd",footer = "asdasd"))
    app.logout()

def test_add_empty_group(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "",header = "",footer = ""))
    app.logout()