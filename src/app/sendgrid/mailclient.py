import os
from typing import List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
from app.config.api_config import apiConfig


async def sendMail(arg_from_email, arg_to_emails: List, arg_subject, arg_htmlBody):
    mail = Mail(
        from_email=arg_from_email,
        subject=arg_subject,
        is_multiple=True,
        html_content=arg_htmlBody,
    )
    generatePersonalization(mail, arg_to_emails)
    try:
        sg = SendGridAPIClient(apiConfig.sendgridApiKey)
        response = sg.send(mail)
    except Exception as e:
        print("Error:", e.message)


def generatePersonalization(mail: Mail, recepients: List):
    for recepient in recepients:
        person = Personalization()
        person.add_to(Email(recepient))
        mail.add_personalization(person)
