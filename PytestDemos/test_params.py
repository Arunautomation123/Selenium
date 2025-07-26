import pytest

@pytest.mark.parametrize("username, password", [("Arun", "Kumar"), ("Pruthivi", "Prasad")])
def test_paramter(username, password):
    print(username, password)

@pytest.mark.parametrize("username", ["Arun", "Prasad"])
def test_paramter_2(username):
    print(username)