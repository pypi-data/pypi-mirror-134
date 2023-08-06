from requests import Session
import requests

requests.packages.urllib3.disable_warnings()


class CVMHttpClientConnector():

    def __init__(self) -> None:
        self.CONNECTOR = Session()

    def get_connector(self):
        return self.CONNECTOR
