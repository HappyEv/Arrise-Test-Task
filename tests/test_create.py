import pytest
from services.crud import BearServices
from test_data import *


@pytest.mark.usefixtures("setup")
class TestCreateServices:
    @pytest.mark.parametrize(
        "types, name, age",
        [
            pytest.param(
                BEAR_TYPES, SAMPLE_NAMES[0], BEAR_AGES["valid"]
            )
        ]
    )
    def test_create_bear(self, types, name, age):
        for i in types:
            bear = BearServices.create(type=i, name=name, age=age)
            params = BearServices.read(bear.id)
            assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower() \
                   and bear.age == params["bear_age"], "Параметры медведя не соответствуют ожидаемым"

    @pytest.mark.parametrize(
        "type, name, age",
        [
            pytest.param(
                BEAR_TYPE_INVALID, SAMPLE_NAMES[0], BEAR_AGES["valid"]
            ),

            pytest.param(
                BEAR_TYPES[0], SAMPLE_NAMES[0], BEAR_AGES["invalid"]
            ),

            pytest.param(
                BEAR_TYPES[0], SAMPLE_NAMES[0], BEAR_AGES["negative"]
            )
        ]
    )
    def test_create_bear_failed(self, type, name, age):
        bear = BearServices.create(type=type, name=name, age=age)
        assert bear is None, "Медвесь создался с невалидными параметрами"
        assert BearServices.read(id) == "EMPTY", "Объект не должен существовать"