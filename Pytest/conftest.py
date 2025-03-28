import pytest

@pytest.fixture(scope="session")
def PreSetupWork():
    print("Here you're in confttest")