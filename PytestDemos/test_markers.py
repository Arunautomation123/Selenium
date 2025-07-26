import pytest
import sys

@pytest.mark.smoke
def test_login():
    print("Login done")

@pytest.mark.regression
def test_addproduct():
    print("Added product")

@pytest.mark.skip(reason="Simple skip")
def test_logout():
    print("Logout done")

@pytest.mark.skipif(sys.version_info<(3,13), reason = "Python version not supported")
def test_narker():
    print("skip if condition")

# intentional failing test feature is not implemented
@pytest.mark.xfail
def test_xfail():
    assert True
    print("testing marker xfail")


def test_close_app():
    assert True
    print("Closing application")