import pytest


@pytest.fixture
def test_fixture():
    print("I run first")
    yield
    print("I run last")

def test_main(test_fixture):
    print("Original method")
