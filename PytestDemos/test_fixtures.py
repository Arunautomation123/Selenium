import pytest

@pytest.fixture()
def setup():
    print("Start the ECU")
    yield
    print("Stop the ECU")

def test_1(setup):
    print("Test 1 is executed")

def test_2(setup):
    print("Test 2 is executed")

def test_3(setup):
    print("Test 3 is executed")