from slack_sdk.webhook import WebhookClient


def send(slackUrl, text):
    print("send slack message to " + slackUrl)
    webhook = WebhookClient(slackUrl)
    response = webhook.send(
        text="fallback",
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
    assert response.body == "ok"
