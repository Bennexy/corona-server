import os
import sys
from flask_restx import Namespace, Resource, fields
from flask import jsonify, request


sys.path.append('.')

from server import api

namespace = Namespace("OcrserverProcess", description="Process requests")

parser_in = api.parser()



@namespace.route("input/")
@namespace.expect(parser_in)
class MyApi(Resource):
    def get(self):
        payload = request.form
        pass


@namespace.route("output/")
class MyApi(Resource):
    def post(self):
        pass

















