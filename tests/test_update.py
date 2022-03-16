import pytest
from services.crud import BearServices
from test_data import *


@pytest.mark.usefixtures("setup")
class TestUpdateServices:
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
