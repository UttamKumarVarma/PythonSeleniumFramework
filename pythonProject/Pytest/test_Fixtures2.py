import pytest


#use fixture from conftest file
def test_main(test_fixture):
    print("Original method")
