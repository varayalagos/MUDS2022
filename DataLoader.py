from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from Criptocurrency import Criptocurrency

#Connection string from api with fake data
API_URL_TEST ='https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
KEY_TEST = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c'

#Connection string from api with real data
API_URL_REAL ='https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
KEY_REAL = 'cfdc673e-2a70-4e0c-ae6c-c1cac3a9f77a'

#Connection string from api to use
API_URL = API_URL_REAL
KEY_API = KEY_REAL
URL_COINBASE = 'https://coinmarketcap.com/api/'

#Json file to store the data
CACHE_FILE_NAME = 'cache.json'

class DataLoader:
    """
    Module for data management functionalities. It is intended to be used to load, store and process the dataset
    """

    @staticmethod
    def import_data_from_api() -> list:
        """
          Method to import the data. By default it loads the data from the coinmarketcap API service. If it is indicated,
          and the file exists, the data can be loaded from a cache file stored in a JSON format. This functionality
          is useful to avoid calling the API service too many times in a short period of time and to work offline.
          :return: The list with the information (I use a limit of 15 to restrict the calls to the api)
        """
        parameters = {
            'start': '1',
            'limit': '20',
            'convert': 'EUR'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': KEY_API,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(API_URL, params=parameters)
            data_api = json.loads(response.text)
            # print(data_api)
        except (ConnectionError, Timeout, TooManyRedirects) as error:
            print(error)

        return data_api['data']

    @staticmethod
    def import_data_from_json() -> list[dict]:
        """
          Method to import data from json file.
         :return: The list of dictionaries with the information needed
        """
        with open(CACHE_FILE_NAME) as f:
            return json.load(f)

    @staticmethod
    def export_data_to_json(data: list[dict]) -> list[dict]:
        """
          Method to export data to json file.
         :return: The list of dictionaries with the information needed
        """
        with open(CACHE_FILE_NAME, 'w') as f:
            return json.dump(data, f, indent=4)

    @staticmethod
    def convert_to_criptocurrency(data: list[dict]) -> list[Criptocurrency]:
        """
        Method to convert the original raw data to a list of Person class items
        :param data: Original raw dataset (list of dictionaries)
        :return: list of processed data
        """

        criptocurrencies = []
        for item in data:
            criptocurrencies.append(Criptocurrency(item))

        return criptocurrencies

