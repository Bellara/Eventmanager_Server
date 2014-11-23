__author__ = 'Henning'

from flask import Flask
from flask import request
from JSONResponse import JSONResponse
from Server.Server import Server
from Server.EventError import EventError

app = Flask(__name__)

@app.route("/user/login")
def user_login():
    resp = JSONResponse()
    try:
        mail = request.args.get("mail")
        pw = request.args.get("pw")

        server = Server()
        data = server.userLogin(mail, pw)

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        resp.setError("Unbekannter Fehler")

    return resp.getFinished()


@app.route("/user/getAll")
def user_getAll():
    #TODO impl
    return "works"


@app.route("/events/getInvitations")
def events_getInvitations():
    #TODO impl
    return "works"


@app.route("/events/getById")
def events_getById():
    #TODO impl
    return "works"


@app.route("/events/invite")
def events_inivite():
    #TODO impl
    return "works"

@app.route("/events/create")
def events_create():
    #TODO impl
    return "works"


@app.route("/events/delete")
def events_delete():
    #TODO impl
    return "works"


@app.route("/events/signin")
def events_signin():
    #TODO impl
    return "works"


@app.route("/user/register")
def user_register():
    #TODO impl
    return "works"


def getUrlParamsAsDict(argv):
    ret = {}

    for arg in argv:
        try:
            ret[arg] = request.args.get(arg)
        except Exception:
            raise Exception("Argument '{}' nicht gefunden!".format(arg))

    return ret

if __name__ == "__main__":
    app.run()