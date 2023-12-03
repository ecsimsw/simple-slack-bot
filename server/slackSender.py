import logging
logging.basicConfig(level=logging.DEBUG)

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="xoxb-2476610625797-6307304308496-J1g9DaDt3bT7xsJ06ZNWhKpN")

def send(text):
    howler_msg = "<@{}> HOW DARE YOU STEAL THAT CAR! I AM ABSOLUTELY DISGUSTED! YOUR FATHER'S IS NOW FACING AN INQUIRY AT WORK, AND IT'S ENTIRELY YOUR FAULT! IF YOU PUT ANOTHER TOE OUT OF LINE, WE'LL BRING YOU STRAIGHT HOME!: \n" \
                 "*<https://github.com/Giggle-projects/our-howler|Github - our howler>*".format("U02DWRS37FY")
    try:
        response = client.chat_postMessage(
            channel="howler-alert",
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": howler_msg
                    }
                }
            ]
        )
        assert response.status_code == 200
    except SlackApiError as e:
        assert e.response["error"]
