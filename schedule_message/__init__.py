import logging
import os
import json
import datetime

import azure.functions as func
from azure.servicebus import ServiceBusClient, ServiceBusMessage


def send_message_to_topic(body):
    print(body)
    servicebus_client = ServiceBusClient.from_connection_string(
        conn_str=os.getenv('SERVICE_BUS_CONNECTION_STRING'),
        logging_enable=True)
    with servicebus_client:
        sender = servicebus_client.get_topic_sender(topic_name='topic1')
        with sender:
            message = ServiceBusMessage(json.dumps(body))
            scheduled_time_utc = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
            #sender.schedule_messages(message, scheduled_time_utc)
            sender.schedule_messages(message, scheduled_time_utc)

    
def main(message: func.ServiceBusMessage):
    # Log the Service Bus Message as plaintext

    message_content_type = message.content_type
    message_body = message.get_body().decode("utf-8")

    logging.info("Python ServiceBus topic trigger processed message.")
    #logging.info("Message Content Type: " + message_content_type)
    logging.info("Message Body: " + message_body)

    send_message_to_topic("Ruidant")
