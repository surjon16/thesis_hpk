from data.models    import Accounts, Roles, Appointments, Status
from data           import db

from flask_login    import login_user, current_user
from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime, timedelta

import requests, json
import os

max_slots = 2 # slots per hour from 9AM to 5PM
daily_slots = 14 # for 7hours at max slots per hour

class AppointmentsRepo:
    
    # ==================================================================================
    # APPOINTMENTS
    
    def readAppointments():
        return Appointments.query.order_by(Appointments.status_id.desc(), Appointments.time_start.asc()).all()
    
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

        data = Appointments.query.filter_by(id=request['id']).first()

        appointment_date = request['appointment_date']
        try:
            appointment_date = datetime.strptime(appointment_date, '%m/%d/%Y') + timedelta(hours=int(request['time']))
        except ValueError:
            appointment_date = request['appointment_date']

        if data == None:
            data = Appointments(
                details             = request['details'],
                appointment_date    = appointment_date,
                assigned            = request['assigned'],
                account_id          = request['account_id'],
                service_id          = request['service_id'],
                status_id           = request['status_id']
            )
            db.session.add(data)

        else:

            data.details             = request['details']
            data.appointment_date    = appointment_date
            data.assigned            = request['assigned']
            data.account_id          = request['account_id']
            data.service_id          = request['service_id']
            data.status_id           = request['status_id']
                
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
