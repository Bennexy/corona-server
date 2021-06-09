import os
from re import S
import sys
import json
import requests
from flask_restx import Namespace, Resource, fields
from flask import jsonify, request


sys.path.append('.')

from server.config import ServerUrl, CoronaServerUrl
from server.tasks.url_get import *
from server.tasks.corona_get import *

from server import api

from server.logger import get_logger

logger = get_logger('corona-server-process')

namespace = Namespace("CoronaServerProcess", description="Process requests")

parser_in = api.parser()
parser_out = api.parser()

parser_in.add_argument("payload", type=dict, required=True, location="form")
parser_out.add_argument("payload", type=dict, required=True, location="form")

@namespace.route("input/")
@namespace.expect(parser_in)
class MyApi(Resource):
    def post(self):
        logger.debug(f'got post request')

        payload = request.json

        logger.debug(f'payload recieved: {payload}')

        data = payload['payload']
        try:
            return jsonify(message="corona server has recieved request and payload")

        finally:

            url_dict = get_corona_url(data)

            logger.debug(f'data from url get: {url_dict}')

            payload_out = get_corona_data(url_dict)

            print(payload_out)

            url = CoronaServerUrl + "/endpoints/upload_to_db/"

            payload_out_send = {"payload": payload_out}

            res = requests.post(url, json=payload_out_send)

            if res.status_code != 200:
                logger.error(f'post to upload data to db corona api failed with statuscode {res.status_code} and text {res.text}')


@namespace.route("upload_to_db/")
@namespace.expect(parser_out)
class MyApi(Resource):
    def post(self):
        logger.debug(f'got post request for upload_to_db')
        try:
            payload = request.json
            
            payload_in = payload['payload']
            logger.debug(f'recieved payload_in {type(payload_in)}')
            return jsonify(message="recieved post")

        finally:

            url = ServerUrl + "/api/db/db_upload/"
            logger.debug(f'created server url {url}')

            payload_out = {"datatype":"corona", "data":payload_in}
            logger.debug(f'created payload_out {payload_out, type(payload_out)} ')

            res = requests.post(url, json=dict(payload_out))
            logger.debug(f'response status code from post to db {res.status_code} text {res.text}')

            if res.status_code != 200:
                logger.error(f'post to upload data to db failed with statuscode {res.status_code} and text {res.text}')

        
















