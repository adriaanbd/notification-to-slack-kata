# This is a sample Python script.
import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
from flask import Flask, request, jsonify
from slack_sdk import WebClient

app = Flask(__name__)
load_dotenv()


@dataclass
class AlertSent:
    sent: bool
    email: Optional[str] = None


def process_notification(payload):
    client = WebClient(token=os.getenv("SLACK_TOKEN"))
    channel_id = os.getenv("CHANNEL_ID")
    email = payload["Email"]

    if payload["Type"] != "SpamNotification":
        return AlertSent(False)

    result = client.chat_postMessage(
        channel=channel_id,
        text=email
    )
    if result.get("ok", False) is False:
        return AlertSent(False)

    return AlertSent(True, email)


@app.route("/", methods=["POST"])
def process_notification_endpoint():
    payload = request.get_json()
    status = 200
    try:
        process_notification(payload)
    except Exception:
        status = 500
    return jsonify(status=status)
