import os
import sys

from flask import Flask, url_for
from flask_restx import Api, Resource

sys.path.append('.')

import server.config as config


api = Api(version="1.4.8",
    title="CloudIntegration - OCR Server",
    contact="sales@fellow-consulting.de",
    description="OCR Server APIs")

app = Flask(__name__)

api.init_app(app)



class MyApi(Api):
    @property
    def specs_url(self):
        """Monkey patch for HTTPS"""
        scheme = "http" if "8001" in self.base_url else "https"
        return url_for(self.endpoint("specs"), _external=True, _scheme=scheme)








from server.namespaces.endpoints import namespace as namespace_endpoints

api.add_namespace(namespace_endpoints, path="/endpoints/")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)







