import pytest

from app import process_notification, AlertSent


@pytest.fixture
def a_payload():
    def _a_payload(
        email="zaphod@example.com",
        type="SpamNotification"
    ):
        payload = {
          "RecordType": "Bounce",
          "Type": type,
          "TypeCode": 512,
          "Name": "Spam notification",
          "Tag": "",
          "MessageStream": "outbound",
          "Description": "The message was delivered, but was either blocked by the user, or classified as spam, bulk mail, or had rejected content.",
          "Email": email,
          "From": "notifications@honeybadger.io",
          "BouncedAt": "2023-02-27T21:41:30Z",
        }
        return payload
    return _a_payload


def test_process_notification(a_payload):
    notification = a_payload()
    response = process_notification(notification)
    assert isinstance(response, AlertSent)
    assert response.sent is True
    assert response.email == notification["Email"]

    another_notification = a_payload(email="random@test.com")
    another_response = process_notification(another_notification)
    assert another_response.email == another_notification["Email"]


def test_process_notification_does_not_send_alert(a_payload):
    an_untyped_notification = a_payload(type="HardBounce")
    response = process_notification(an_untyped_notification)
    assert response.sent is False
