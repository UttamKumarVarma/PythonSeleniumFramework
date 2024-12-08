import pytest


@pytest.mark.smoke
def test_marks1():
    print("Marks1")

@pytest.mark.smoke
@pytest.mark.skip
def test_marks2():
    print("marks2")

@pytest.mark.smoke
def test_marks3():
    print("marks3")

@pytest.mark.smoke
@pytest.mark.xfail
def test_marks3():
    print("marks4")