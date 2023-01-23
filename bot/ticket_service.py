import requests

from .config import Setting as settings


def set_session_id():
    url = settings.SESSION_ID_URL
    payload = {
        'inn': settings.INN,
        'client_secret': settings.CLIENT_SECRET,
        'password': settings.PASSWORD
    }
    resp = requests.post(url, json=payload, headers=settings.HEADERS)
    return resp.json()['sessionId']


def get_ticket_id(session_id, qr_code: str) -> str:
    url = settings.TICKET_URL
    payload = {'qr': qr_code}
    settings.HEADERS['sessionId'] = session_id
    try:
        resp = requests.post(url, json=payload, headers=settings.HEADERS)
        ticket_id = resp.json()["id"]
    except Exception as error:
        print(error)
    else:
        return ticket_id

def get_ticket(session_id, ticket_id):
    url = settings.TICKET_ID_URL + f'/{ticket_id}'
    settings.HEADERS['sessionId'] = session_id
    settings.HEADERS['Content-Type'] = 'application/json'
    resp = requests.get(url, headers=settings.HEADERS)
    return resp.json()

def get_receipt(data):
    session_id = set_session_id()
    ticket_id = get_ticket_id(session_id, data)
    receipt_data = get_ticket(session_id, ticket_id)
    return receipt_data