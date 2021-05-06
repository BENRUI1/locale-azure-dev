import logging

import azure.functions as func
import json
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = 'http://10.20.13.241:8315/imx_services/token?apiKey=ACP_TEST_12345XXZZ'

    logging.info('Get token')
    response = requests.get(url)
    data = response.json()
    token = data["sessionKey"]
    
    logging.info('token : ' + token)

    return func.HttpResponse(
        json.dumps(token),
        mimetype="application/json",
        status_code=200)




