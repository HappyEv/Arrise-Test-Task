import pytest
from services.crud import BearServices


@pytest.mark.usefixtures("setup")
class TestReadServices:
    def test_get_info(self):
        info = BearServices.info()
        assert info != "", "Info shouldn't be empty"

    def test_read_nonexistent(self, id):
        assert BearServices.read(id) == "EMPTY", "Expected EMPTY response"
