from data.models    import Accounts, Roles, Appointments, Status
from data           import db

from flask_login    import login_user, current_user
from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime

class StatusRepo:
    
    # ==================================================================================
    # STATUS

    def readAllStatus():
        return Status.query.all()

    def readStatus(id):
        return Status.query.filter_by(id=id).first()

    def upsertStatus(request):

        data = Status.query.filter_by(id=request['id']).first()

        if data == None:
            data = Status(
                status  = request['status']
            )
            db.session.add(data)
        else:
            data.status  = request['status']

        db.session.commit()

        return True

    def deleteStatus(request):

        data = Status.query.filter_by(id=request['id']).first()

        if data == None:
            return False
        else:
            db.session.delete(data)
            db.session.commit()
            return True
