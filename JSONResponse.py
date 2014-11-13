__author__ = 'Henning'

import json
from flask import Response


class JSONResponse():
    """

    Einfache Klasse zur Erzeugung der JSON Antworten..
    """
    JSON_MIMETYPE = "application/json"

    def __init__(self, success=None, message=None, data=None):
        self.success = success
        self.message = message
        self.data = data
        return

    def setError(self, message="Unbekannter Fehler"):
        self.message = message
        self.success = False
        self.data = {}
        return

    def setSuccess(self, data={}):
        self.success = True
        self.message = ""
        self.data = data

    def getFinished(self):
        if self.success:
            return Response(response=json.dumps({"result": {"status": "success", "message": ""}, "data": self.data}),
                            mimetype=JSONResponse.JSON_MIMETYPE)
        else:
            return Response(response=json.dumps({"result": {"status": "error", "message": self.message}, "data": {}}),
                            mimetype=JSONResponse.JSON_MIMETYPE)