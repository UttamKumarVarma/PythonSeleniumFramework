import pytest


@pytest.mark.usefixtures("test_fixture")
class TestExample:

    def test_fix1(self):
        print("I run middle")

    def test_fix2(self2):
        print("I run middle")
