import logging

import azure.functions as func
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    message = Mail(
        from_email='nathalie.ruidant@atradius.com',
        to_emails='nruidant@hotmail.com',
        subject='Sending with Twilio SendGrid is Fun - New',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        logging.info(response.status_code)
        logging.info(response.body)
        logging.info(response.headers)
        return func.HttpResponse(
            "e-mail sent using sendgrid API",
            status_code=200
        )
    except Exception as e:
        logging.info(e.message)
        return func.HttpResponse(
            "Error sending mail with sendgrid API",
            status_code=401
        )
