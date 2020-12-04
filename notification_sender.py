import requests


class SendNotification:
    def __init__(self, token, chat_id, notification_text):
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        data = {'chat_id': {chat_id}, 'text': notification_text}
        requests.post(url, data).json()
