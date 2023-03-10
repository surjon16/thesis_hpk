from data.models    import Accounts, Appointments, Consultations, Purpose, Roles, Status
from data           import db

from flask_login    import login_user, current_user
from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime, timedelta

import requests, json
import os

class QueuesRepo:
    
    # ==================================================================================
    # APPOINTMENTS
    
    def readAppointments():
        return Appointments.query.order_by(Appointments.status_id.desc(), Appointments.created_at.asc()).all()
    
    def readAppointment(id):
        return Appointments.query.filter_by(id=id).first()

    def readAvailableSlots():

        appointments = db.session.query(Appointments.appointment_date).filter(or_(Appointments.status_id==1, Appointments.status_id==4)).all()
        data = appointments if appointments is not None else []

        daily = [i.appointment_date.strftime('%m/%d/%Y') for i in data]
        dailylist = list(set(daily))

        hourly = [i.appointment_date for i in data]
        hourlylist = list(set(hourly))
        hourlydata = [{
            'dt': h,
            'd' : h.strftime('%m/%d/%Y'),
            'h' : h.strftime('%I:%M%p') + '-' + (h + timedelta(hours=1)).strftime('%I:%M%p')
        } for h in hourlylist]        
        
        return [{
            'slots' : daily_slots - daily.count(i),
            'date'  : i,
            'time'  : [{
                't' : t['h'],
                'slots' : max_slots - hourly.count(t['dt'])
            } for t in hourlydata if t['d'] == i]
        } for i in dailylist]

    def readSchedules():

        appointments = db.session.query(Appointments.appointment_date).filter(or_(Appointments.status_id==1, Appointments.status_id==4)).all()
        datalist = list(set(appointments if appointments is not None else []))

        schedules = [{
                'datetime' : data.appointment_date,
                'date': data.appointment_date.strftime('%m/%d/%Y'), 
                'time': data.appointment_date.strftime('%I:%M%p') + '-' + (data.appointment_date + timedelta(hours=1)).strftime('%I:%M%p'),
                'slots': max_slots - appointments.count(data)
            } for data in datalist]

        return schedules

    def updateAppointmentStatus(request):

        data = Appointments.query.filter_by(id=request['id']).first()
        data.status_id = request['status_id']

        db.session.commit()

        return True

    def upsertAppointment(request):
        
        # appointment = Appointments(
        #     time_start      = Consultations.query.filter_by(id=1).first().time_start,
        #     time_end        = Consultations.query.filter_by(id=1).first().time_end,
        #     priority        = Accounts.query.filter_by(role_id=2).first().last_name + str(Appointments.query.count() + 1),
        #     participants    = Accounts.query.filter(Accounts.id.in_([2,3])).all(),
        #     status_id       = Status.query.filter_by(status="Pending").first().id,
        #     purpose_id      = Purpose.query.filter_by(purpose="Capstone").first().id
        # )
        # db.session.add(appointment)

        data = Appointments.query.filter_by(id=request['id']).first()

        if data == None:

            

            data = Appointments(
                priority        = request['priority'],
                participants    = Accounts.query.filter(Accounts.id.in_(request['participants'])).all(),
                status_id       = request['status_id'],
                purpose_id      = request['purpose_id'],
            )
            db.session.add(data)

        else:

            priority        = request['priority']
            participants    = Accounts.query.filter(Accounts.id.in_(request['participants'])).all()
            status_id       = request['status_id']
            purpose_id      = request['purpose_id']
                
        db.session.commit()

        return True

    def deleteAppointment(request):

        data = Appointments.query.filter_by(id=request['id']).first()
        
        if data == None:
            return False
        else:
            db.session.delete(data)
            db.session.commit()
            return True

    def tester():
        pass
