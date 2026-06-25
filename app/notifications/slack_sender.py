import requests

from app.config import SLACK_WEBHOOK


def send_slack(message):

    try:

        response = requests.post(
            SLACK_WEBHOOK,
            json={
                "text": message[:3000]
            }
        )

        print(
            "Slack:",
            response.status_code,
            response.text
        )

    except Exception as e:

        print(
            "Slack Error:",
            str(e)
        )