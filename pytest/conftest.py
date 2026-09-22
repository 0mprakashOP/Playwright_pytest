import pytest

@pytest.fixture(scope="module", autouse=True)
def pretest_module():
    print("tested pretest module")
    yield
    print("teardown fixture module")
    return "OK"

@pytest.fixture(scope="session")
def pretest_session():
    print("tested pretest session")
