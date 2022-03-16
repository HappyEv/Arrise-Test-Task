import pytest
from services.crud import BearServices
from constants import BEAR_TYPES


@pytest.mark.usefixtures("setup")
class TestBearServices:
    def test_get_info(self):
        info = BearServices.info()
        assert info is not None

    @pytest.mark.parametrize(
        "types, name, age",
        [
            pytest.param(
                BEAR_TYPES, "misha", 3
            )
        ]
    )
    def test_create_bear(self, types, name, age):
        for i in types:
            bear = BearServices.create(type=i, name=name, age=age)
            params = BearServices.read(bear.id)
            assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower()\
                and bear.age == params["bear_age"]

    @pytest.mark.parametrize(
        "type, name, age",
        [
            pytest.param(
                "WHAT", "misha", 3
            ),

            pytest.param(
                "BLACK", "misha", "what"
            ),

            pytest.param(
                "BLACK", "misha", -1
            )
        ]
    )
    def test_create_bear_failed(self, type, name, age):
        bear = BearServices.create(type=type, name=name, age=age)
        assert bear is None

    @pytest.mark.parametrize(
        "type, name, age, new_params",
        [
            pytest.param(
                "BLACK", "misha", 3,
                {
                    "bear_type": "POLAR",
                    "bear_name": "misha",
                    "bear_age": 3
                }
            ),

            pytest.param(
                "BLACK", "misha", 3,
                {
                    "bear_type": "BLACK",
                    "bear_name": "sasha",
                    "bear_age": 3
                }
            ),

            pytest.param(
                "BLACK", "misha", 3,
                {
                    "bear_type": "BLACK",
                    "bear_name": "misha",
                    "bear_age": 99
                }
            )
        ]
    )
    def test_update_bear(self, type, name, age, new_params):
        bear = BearServices.create(type=type, name=name, age=age)
        params = BearServices.read(bear.id)
        assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower()\
               and bear.age == params["bear_age"]

        assert BearServices.update(bear, new_params)
        params = BearServices.read(bear.id)
        assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower()\
               and bear.age == params["bear_age"]

    @pytest.mark.parametrize(
        "type, name, age, new_params",
        [
            pytest.param(
                "BLACK", "misha", 3,
                {
                    "bear_type": "what",
                }
            ),

            pytest.param(
                "BLACK", "misha", 3,
                {
                    "bear_age": "what"
                }
            )
        ]
    )
    def test_update_bear_failed(self, type, name, age, new_params):
        bear = BearServices.create(type=type, name=name, age=age)
        params = BearServices.read(bear.id)
        assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower() and bear.age == params[
            "bear_age"]
        assert not BearServices.update(bear, new_params)

    @pytest.mark.parametrize(
        "type, name, age, amount",
        [
            pytest.param(
                "BLACK", "misha", 3, 10
            )
        ]
    )
    def test_delete_all(self, type, name, age, amount):
        for i in range(amount):
            bear = BearServices.create(type=type, name=name, age=age)
            params = BearServices.read(bear.id)
            assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower() and bear.age == params[
                "bear_age"]
        assert BearServices.delete()
        assert BearServices.read() == []

    @pytest.mark.parametrize(
        "type, name, age",
        [
            pytest.param(
                "BLACK", "misha", 3
            )
        ]
    )
    def test_delete_specific(self, type, name, age):
        bear = BearServices.create(type=type, name=name, age=age)
        params = BearServices.read(bear.id)
        assert bear.type == params["bear_type"] and bear.name == params["bear_name"].lower()\
               and bear.age == params["bear_age"]
        assert BearServices.delete(bear.id) is True
        assert BearServices.read(bear.id) == "EMPTY"

    @pytest.mark.parametrize(
        "id",
        [
            pytest.param(-1),
            pytest.param(0),
            pytest.param(1),
            pytest.param("abc"),
        ]
    )
    def test_delete_nonexistent(self, id):
        assert BearServices.delete(id)

    @pytest.mark.parametrize(
        "id",
        [
            pytest.param(-1),
            pytest.param(0),
            pytest.param(1),
            pytest.param("abc"),
        ]
    )
    def test_read_nonexistent(self, id):
        assert BearServices.read(id) == "EMPTY"


