
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from models import EmailRequest
import logging

def send_email(email: EmailRequest):
    try:
        
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login('ramazan.aitimovkz@gmail.com', 'qfjs twtj qirn kktl')

        
        msg = MIMEMultipart()
        msg['From'] = 'ramazan.aitimovkz@gmail.com'
        msg['To'] = email.to
        msg['Subject'] = email.subject

        
        msg.attach(MIMEText(email.message, 'plain'))

        
        smtp_server.sendmail('ramazan.aitimovkz@gmail.com', email.to, msg.as_string())
        smtp_server.quit()

        
        logging.info("Email sent successfully")

        return {"message": "Email sent successfully"}
    except Exception as e:
       
        logging.error(f"An error occurred: {str(e)}")
        raise e
