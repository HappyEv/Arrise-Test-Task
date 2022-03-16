import pytest
from services.crud import BearServices
from models.bear import Bear
from test_data import *


@pytest.fixture(scope="function")
def setup():
    BearServices.delete()
    yield
    BearServices.delete()


@pytest.fixture()
def good_bear():
    bear = BearServices.create(BEAR_TYPES[0], SAMPLE_NAMES[0], BEAR_AGES["valid"])
    params = BearServices.read(bear.id)
    assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower() \
           and bear.age == params["bear_age"], "Параметры медведя не соответствуют ожидаемым"
    return bear
