import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")


class Readconfig:

    @staticmethod
    def GetLoginUrl():
        url = config.get('setup', 'url')
        return url

    @staticmethod
    def GetUserName():
        username = config.get('setup', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('setup', 'password')
        return password

    @staticmethod
    def get_symbol():
        symbol = config.get('trade', 'symbol')
        return symbol

    @staticmethod
    def get_quantity():
        quantity = config.get('trade', 'quantity')
        return quantity

