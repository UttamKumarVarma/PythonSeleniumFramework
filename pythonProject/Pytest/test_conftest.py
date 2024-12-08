import pytest


@pytest.fixture(scope="class")
def test_fixture():
    print("I run first")
    yield
    print("I run last")

@pytest.fixture()
def data():
    return ["Uttam Kumar Varma","Vummididevu","uttamkumarvarma.github.io"]


# first data contains 3 values. Next contains 2
@pytest.fixture(params=[("Uttam", "Kumar", "Varma"), ("Arg2", "Arg3")])
def data2(request):
    return request.param