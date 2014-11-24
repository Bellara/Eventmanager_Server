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

        if mail is None or pw is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        data = server.userLogin(mail, pw)

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


@app.route("/user/getAll")
def user_getAll():
    resp = JSONResponse()
    try:
        server = Server()
        data = server.getAllUsers()

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


@app.route("/events/getInvitations")
def events_getInvitations():
    #TODO impl
    return "works"


@app.route("/events/getById")
def events_getById():
    resp = JSONResponse()

    try:
        id = str(request.args.get("id"))

        if id is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        data = server.getEventById(id)

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


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
    resp = JSONResponse()

    try:
        mail = str(request.args.get("mail"))
        pw = str(request.args.get("passwort"))
        name = str(request.args.get("name"))
        vorname = str(request.args.get("vorname"))

        if mail is None or pw is None or name is None or vorname is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        data = server.registerUser(mail, name, vorname, pw)

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


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