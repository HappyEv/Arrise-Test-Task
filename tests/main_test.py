import pytest
from services.crud import BearServices
from test_data import *


@pytest.mark.usefixtures("setup")
class TestBearServices:
    def test_get_info(self):
        info = BearServices.info()
        assert info != "", "Сообщение пустое"

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

    @pytest.mark.parametrize(
        "new_params",
        [
            pytest.param(
                {
                    "bear_type": BEAR_TYPES[1],
                    "bear_name": SAMPLE_NAMES[0],
                    "bear_age": BEAR_AGES["valid"]
                }
            ),

            pytest.param(
                {
                    "bear_type": BEAR_TYPES[0],
                    "bear_name": SAMPLE_NAMES[1],
                    "bear_age": BEAR_AGES["valid"]
                }
            ),

            pytest.param(
                {
                    "bear_type": BEAR_TYPES[0],
                    "bear_name": SAMPLE_NAMES[0],
                    "bear_age": BEAR_AGES["valid"] + 1
                }
            )
        ]
    )
    def test_update_bear(self, new_params, good_bear):
        assert BearServices.update(good_bear, new_params), "Ожидался положительный ответ от сервиса"
        params = BearServices.read(good_bear.id)
        assert good_bear.type == params["bear_type"] and good_bear.name == params["bear_name"].lower() \
               and good_bear.age == params["bear_age"], "Параметры медведя не соответствуют ожидаемым"

    @pytest.mark.parametrize(
        "new_params",
        [
            pytest.param(
                {
                    "bear_type": BEAR_TYPE_INVALID,
                }
            ),

            pytest.param(
                {
                    "bear_age": BEAR_AGES["invalid"]
                }
            )
        ]
    )
    def test_update_bear_failed(self, new_params, good_bear):
        assert not BearServices.update(good_bear, new_params), "Ожидался отрицательный ответ от сервиса"

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

    @pytest.mark.parametrize(
        "id",
        [
            pytest.param(IDS["positive"]),
            pytest.param(IDS["zero"]),
            pytest.param(IDS["negative"]),
            pytest.param(IDS["string"]),
        ]
    )
    def test_read_nonexistent(self, id):
        assert BearServices.read(id) == "EMPTY", "Объект не должен существовать"
