import pytest
from services.crud import BearServices


@pytest.fixture(scope="function")
def setup():
    BearServices.delete()
    yield
    BearServices.delete()
