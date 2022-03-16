import requests
from config import CONFIG
from models.bear import Bear


class BearServices:
    @staticmethod
    def create(type, name, age):
        """Функция создает объект медведя с заданными параметрами
        Args:
            :param type Тип медведя
            :param name Имя медведя
            :param age Возраст медведя

        Returns:
            Если создание успешно:
                bear: Объект медведя
            Иначе None
        """
        params = {"bear_type": type, "bear_name": name, "bear_age": age}
        response = requests.post(CONFIG["BASE_URL"] + CONFIG["BEAR_ENDPOINT"], json=params)
        if response:
            id = int(response.text)
            bear = Bear(id=id, age=age, name=name, type=type)
            return bear
        else:
            return None

    @staticmethod
    def delete(id=None):
        """Функция удаляет объект медведя по его номеру, либо все объекты, если номер не задан
        Args:
            :param id Номер медведя

        Returns:
            Если удаление успешно:
                True
            Иначе
                False
        """
        if id is None:
            response = requests.delete(CONFIG["BASE_URL"] + CONFIG["BEAR_ENDPOINT"])
        else:
            response = requests.delete(CONFIG["BASE_URL"] + CONFIG["BEAR_ENDPOINT"] + "/" + str(id))
        if response:
            return True
        else:
            return False

    @staticmethod
    def read(id=None):
        """Функция считывает содержимое объекта медведя по его номеру, либо все объекты, если номер не задан
        Args:
            :param id Номер медведя

        Returns:
            Если объект пустой:
                "EMPTY"
            Иначе
                Содержимое объекта
        """
        if id is None:
            response = requests.get(CONFIG["BASE_URL"] + CONFIG["BEAR_ENDPOINT"])
        else:
            response = requests.get(CONFIG["BASE_URL"] + CONFIG["BEAR_ENDPOINT"] + "/" + str(id))
        if response.text == "EMPTY":
            return response.text
        else:
            return response.json()

    @staticmethod
    def update(bear, params):
        """Функция обновляет содержимое объекта медведя по заданным параметрам
        Args:
            :param bear Объект медведя
            :param params Параметры медведя

        Returns:
            Если обновление успешно:
                True
            Иначе
                False
        """
        response = requests.put(CONFIG["BASE_URL"] + CONFIG["BEAR_ENDPOINT"] + "/" + str(id), json=params)
        if response:
            bear.type = params["bear_type"]
            bear.name = params["bear_name"]
            bear.age = params["bear_age"]
            return True
        else:
            return False

    @staticmethod
    def info():
        """Функция возвращает информацию об API сервиса

        Returns:
            Содержимое текста
        """
        return requests.get(CONFIG["BASE_URL"] + CONFIG["INFO_ENDPOINT"]).text
