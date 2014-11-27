__author__ = 'Henning'

from flask import Flask
from flask import request
from globals import DEBUG
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
    resp = JSONResponse()

    try:
        uid = str(request.args.get("uid"))

        if uid is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        data = server.getInvitations(uid)

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        if DEBUG:
            resp.setError(str(e))
        else:
            resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


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
        if DEBUG:
            resp.setError(str(e))
        else:
            resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


@app.route("/events/invite")
def events_inivite():
    resp = JSONResponse()

    try:
        eid = str(request.args.get("eid"))
        uid = str(request.args.get("uid"))
        aid = str(request.args.get("aid"))

        if eid is None or uid is None or aid is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        server.invite(eid, aid, uid)

        resp.setSuccess()

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        if DEBUG:
            resp.setError(str(e))
        else:
            resp.setError(EventError.UNDEFINED)

    return resp.getFinished()

@app.route("/events/create")
def events_create():
    resp = JSONResponse()

    try:
        admin_id = str(request.args.get("aid"))
        time = str(request.args.get("time"))
        time = time.replace("_", " ")
        bz = str(request.args.get("bz"))
        location = str(request.args.get("Ort"))

        if admin_id is None or time is None or bz is None or location is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        data = server.createEvent(admin_id, time, bz, location)

        resp.setSuccess(data)

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        if DEBUG:
            resp.setError(str(e))
        else:
            resp.setError(EventError.UNDEFINED)

    return resp.getFinished()


@app.route("/events/delete")
def events_delete():
    resp = JSONResponse()

    try:
        eid = str(request.args.get("eid"))
        aid = str(request.args.get("aid"))

        if eid is None or aid is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        server.deleteEvent(aid, eid)

        resp.setSuccess()

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        if DEBUG:
            resp.setError(str(e))
        else:
            resp.setError(EventError.UNDEFINED)

    return resp.getFinished()



@app.route("/events/signin")
def events_signin():
    resp = JSONResponse()

    try:
        eid = str(request.args.get("eid"))
        uid = str(request.args.get("uid"))
        status = str(request.args.get("status"))

        if eid is None or uid is None or status is None:
            raise EventError(EventError.ARGUMENT_ERROR)

        server = Server()
        server.signin(eid, uid, status)

        resp.setSuccess()

    except EventError as e:
        resp.setError(str(e))

    except Exception as e:
        if DEBUG:
            resp.setError(str(e))
        else:
            resp.setError(EventError.UNDEFINED)

    return resp.getFinished()

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


if __name__ == "__main__":
    app.run()