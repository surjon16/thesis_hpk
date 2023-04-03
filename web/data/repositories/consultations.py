from data.models    import Accounts, Consultations, Roles, Appointments, Status
from data           import db

from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime

class ConsultationsRepo:
    # ==================================================================================
    # CONSULTATIONS

    def readConsultations():
        return Consultations.query.all()

    def readConsultation(id):
        return Consultations.query.filter_by(id=id).first()

    def readAccountConstultations(id):
        return Consultations.query.filter_by(account_id=id).all()

    def upsertConsultation(request):

        data = Consultations.query.filter_by(id=request['id']).first()

        if data == None:
            
            data = Consultations(
                time_start  = '1990-01-01 ' + request['time_start'] + ':00',
                time_end    = '1990-01-01 ' + request['time_end'] + ':00',
                account_id  = request['faculty'],
                day         = request['day'],
                room        = request['room'],
            )

            db.session.add(data) 
            db.session.commit() 

            return data

        else:

            data.time_start = '1990-01-01 ' + request['time_start'] + ':00'
            data.time_end   = '1990-01-01 ' + request['time_end'] + ':00'
            data.account_id = request['faculty']
            data.day        = request['day']
            data.room       = request['room']

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
