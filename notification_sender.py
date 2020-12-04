import requests


class SendNotification:
    def __init__(self, token, chat_id, notification_text):
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        data = {'chat_id': {chat_id}, 'text': notification_text}
        requests.post(url, data).json()


# SendNotification("1407892120:AAFbCeviLIjiglgTgEl_UUYnHInD_odilso", 1472327697, "Test Message")