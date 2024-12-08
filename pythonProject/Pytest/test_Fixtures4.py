import pytest


@pytest.mark.usefixtures("data")
class TestFixtures4:
    def test_data(self, data):
        print(data)


def test_uttam(data2):
    print(data2)
    print("data printed")



