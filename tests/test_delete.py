import pytest
from services.crud import BearServices
from test_data import *


@pytest.mark.usefixtures("setup")
class TestBearServices:
    @pytest.mark.parametrize(
        "type, name, age, amount",
        [
            pytest.param(
                BEAR_TYPES[0], SAMPLE_NAMES[0], BEAR_AGES["valid"], AMOUNT_OF_BEARS
            )
        ]
    )
    def test_delete_all(self, type, name, age, amount):
        for i in range(amount):
            bear = BearServices.create(type=type, name=name, age=age)
            params = BearServices.read(bear.id)
            assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower() and bear.age == params[
                "bear_age"], "Параметры медведя не соответствуют ожидаемым"
        assert BearServices.delete(), "Ожидался положительный ответ от сервиса"
        assert BearServices.read() == [], "После удаления не должно оставаться объектов медведей"

    def test_delete_specific(self, good_bear):
        assert BearServices.delete(good_bear.id), "Ожидался положительный ответ от сервиса"
        assert BearServices.read(good_bear.id) == "EMPTY", "Объект не должен существовать"

    @pytest.mark.parametrize(
        "id",
        [
            pytest.param(IDS["positive"]),
            pytest.param(IDS["zero"]),
            pytest.param(IDS["negative"]),
            pytest.param(IDS["string"]),
        ]
    )
    def test_delete_nonexistent(self, id):
        assert BearServices.delete(id), "Ожидался положительный ответ от сервиса"
