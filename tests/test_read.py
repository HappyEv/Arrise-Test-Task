import pytest
from services.crud import BearServices
from test_data import *


@pytest.mark.usefixtures("setup")
class TestReadServices:
    def test_get_info(self):
        info = BearServices.info()
        assert info != "", "Сообщение пустое"

    def test_read_nonexistent(self, id):
        assert BearServices.read(id) == "EMPTY", "Объект не должен существовать"
