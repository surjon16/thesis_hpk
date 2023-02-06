from data.models    import Accounts, Consultations, Roles, Appointments, Status
from data           import db

from flask_login    import login_user, current_user
from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime

class ConsultationsRepo:
    # ==================================================================================
    # CONSULTATIONS

    def readConsultations():
        return Consultations.query.all()

    def readAccountConstultations(id):
        return Consultations.query.filter_by(faculty=id).all()

    def upsertConsultation(request):

        data = Consultations.query.filter_by(id=request['id']).first()

        if data == None:
            
            data = Consultations(
                time_start  = request['time_start'],
                time_end    = request['time_end'],
                faculty     = request['faculty'],
                day         = request['day'],
            )

            db.session.add(data) 
            db.session.commit() 

            return data

        else:

            data.time_start = request['time_start']
            data.time_end   = request['time_end']
            data.faculty    = request['faculty']
            data.day        = request['day']

            db.session.commit()

        return data

    def deleteConsultation(request):

        data = Consultations.query.filter_by(id=request['id']).first()
        
        if data == None:
            return False
        
        else:

            db.session.delete(data)
            db.session.commit()

            return True
