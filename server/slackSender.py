import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="${YOUR_SLACK_BOT_OAUTH_TOKEN}")

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
