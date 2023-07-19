import pytest


@pytest.fixture(scope='module')
def my_fixture():
    print("pre-req:before execution")
    yield
    print("tear-down:after execution")


@pytest.mark.smoke
def test_smoke_1(my_fixture):
    print("test_smoke_1 pass")


@pytest.mark.smoke
@pytest.mark.sanity
def test_sanity_1(my_fixture):
    print("test_sanity_1 pass")
    print("test_smoke_2 pass")
    a = 0
    assert a == 1, "a should be 0"
