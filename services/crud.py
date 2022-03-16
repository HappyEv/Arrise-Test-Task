import requests
from config import CONFIG
from models.bear import Bear


class BearServices:
    @staticmethod
    def create(type, name, age):
        """
        Function creates a bear object with given parameters
        Args:
            :param type
            :param name
            :param age

        Returns:
            If: positive response:
                bear: Bear object
            else: None
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
        """
        Function deletes a bear object with given ID, or all bears, if ID isn't specified
        Args:
            :param id

        Returns:
            If: positive response:
                True
            Else:
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
        """
        Function reads contents of a bear object with given id, or of all bears, if id not specified
        Args:
            :param id

        Returns:
            If there's no object:
                "EMPTY"
            Else:
                Bear's content
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
        """
        Function updated parameters of a given bear

        Args:
            :param bear
            :param params

        Returns:
            If positive response:
                True
            Else:
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
        """
        Function returns info about API

        Returns:
            Text content
        """
        return requests.get(CONFIG["BASE_URL"] + CONFIG["INFO_ENDPOINT"]).text
