import os

from dotenv import load_dotenv

load_dotenv()

class Setting():
    DB_URL = os.getenv('DB_URL')
    HOST = 'irkkt-mobile.nalog.ru:8888'
    SESSION_ID_URL = f'https://{HOST}/v2/mobile/users/lkfl/auth'
    TICKET_URL = f'https://{HOST}/v2/ticket'
    TICKET_ID_URL = f'https://{HOST}/v2/tickets'
    INN = os.getenv('INN')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    PASSWORD = os.getenv('PASSWORD')
    HEADERS = {
        'Host': HOST,
        'Accept': '*/*',
        'Device-OS': 'iOS',
        'Device-Id': '7C82010F-16CC-446B-8F66-FC4080C66521',
        'clientVersion': '2.9.0',
        'Accept-Language': 'ru-RU;q=1, en-US;q=0.9',
        'User-Agent': 'billchecker/2.9.0 (iPhone; iOS 13.6; Scale/2.00)',
    }