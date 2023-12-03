import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-2476610625797-6307304308496-J1g9DaDt3bT7xsJ06ZNWhKpN")

def send(channel, text):
    try:
        response = client.chat_postMessage(
            channel= channel,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": text
                    }
                }
            ]
        )
        assert response.status_code == 200
    except SlackApiError as e:
        assert e.response["error"]
