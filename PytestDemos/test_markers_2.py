import pytest

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.regression
def test_addproduct():
    print("Added product")

@pytest.mark.smoke
def test_logout():
    print("Logout done")