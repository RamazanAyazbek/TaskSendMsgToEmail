from fastapi import FastAPI, HTTPException
from email_service import send_email
from models import EmailRequest

app = FastAPI()


@app.post("/send_email", response_model=dict)
def send_email_route(email: EmailRequest):
    try:
        result = send_email(email)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))