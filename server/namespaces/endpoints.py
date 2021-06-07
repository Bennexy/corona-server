import os
import sys
import json
import requests
from flask_restx import Namespace, Resource, fields
from flask import jsonify, request


sys.path.append('.')

from server.config import ServerUrl
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


@namespace.route("upload_to_db/")
@namespace.expect(parser_out)
class MyApi(Resource):
    def post(self):
        logger.debug(f'got post request')

        payload = request.json
        
        payload_in = payload['payload']

        # url = pass
















