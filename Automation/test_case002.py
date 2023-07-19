import pytest


@pytest.mark.regression
def test_reg():
    print("test_003 pass")


@pytest.mark.smoke
def test_smoke_3():
    print("smoke_3 pass")


a = 103


# @pytest.mark.skip("will execute after fix")  #--> skipped with reason
@pytest.mark.skipif(a > 100, reason="a should 100")  # skipped conditionally
def test_004():
    print("test_004 pass")
