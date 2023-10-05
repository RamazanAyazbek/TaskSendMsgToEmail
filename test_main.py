import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

@pytest.mark.parametrize("email_data", [
    {"to": "ramazan.ayazbek.kz@gmail.com", "subject": "Test email", "message": "This is a test email."},
    
])


def test_send_email(email_data):
    response = client.post("/send_email", json=email_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Email sent successfully"}

def test_send_email_invalid_email():
    invalid_email_data = {"to": "invalid-email", "subject": "Test email", "message": "This is a test email."}
    response = client.post("/send_email", json=invalid_email_data)
    assert response.status_code == 422  # Ожидаем ошибку валидации
    assert "value is not a valid email address" in response.text

# def test_send_email_smtp_error():
#    
#     # app.dependency_overrides[get_smtp_server_settings] = override_smtp_server_settings
#     response = client.post("/send_email", json={"to": "recipient@example.com", "subject": "Test email", "message": "This is a test email."})
#     assert response.status_code == 500
#     assert "SMTPConnectError" in response.text

def override_smtp_server_settings():
    
    return SMTPServerSettings(
        host="invalid-host",
        port=587,
        username="invalid-username",
        password="invalid-password",
    )