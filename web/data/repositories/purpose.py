from data.models    import Accounts, Roles, Appointments, Purpose
from data           import db

from flask_login    import login_user, current_user
from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime

class PurposeRepo:
    
    # ==================================================================================
    # STATUS

    def readAllPurpose():
        return Purpose.query.all()

    def readPurpose(id):
        return Purpose.query.filter_by(id=id).first()

    def upsertPurpose(request):

        data = Purpose.query.filter_by(id=request['id']).first()

        if data == None:
            data = Purpose(
                purpose  = request['purpose']
            )
            db.session.add(data)
        else:
            data.purpose  = request['purpose']

        db.session.commit()

        return True

    def deletePurpose(request):

        data = Purpose.query.filter_by(id=request['id']).first()

        if data == None:
            return False
        else:
            db.session.delete(data)
            db.session.commit()
            return True
