import logging
import requests
import json

import azure.functions as func


def main(message: func.ServiceBusMessage):
    # Log the Service Bus Message as plaintext

    message_content_type = message.content_type
    message_body = message.get_body().decode("utf-8")

    logging.info("Python ServiceBus topic trigger processed message.")
    #logging.info("Message Content Type: " + message_content_type)
    logging.info("Message Body: " + message_body)

    url = 'https://nathdev.azurewebsites.net/api/scoreToken'

    logging.info('Call Get token')
    response = requests.get(url)
    data = response.json()
    logging.info(data)
