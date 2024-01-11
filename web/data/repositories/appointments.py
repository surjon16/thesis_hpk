from data.models    import Accounts, Appointments, Status
from data           import db

from sqlalchemy     import extract, or_, and_, func
from datetime       import datetime

class AppointmentsRepo:
    
    # ==================================================================================
    # APPOINTMENTS
    
    def readAppointments():
        return Appointments.query.order_by(Appointments.status_id.desc(), Appointments.schedule.asc()).all()
    
    def exportAppointments(request):
        return Appointments.query.order_by(Appointments.status_id.desc(), Appointments.schedule.asc()).all()
    
    def readAppointment(id):
        return Appointments.query.filter_by(id=id).first()
    
    def readCall(id):
        return Appointments.query.filter(and_(Appointments.status_id==3, Appointments.account_id==id, func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.id.asc()).first()

    def readCalls():
        # return Appointments.query.filter(and_(Appointments.status_id.in_([2,3]), func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.updated_at.desc()).all()
        return Appointments.query.filter(and_(Appointments.status_id.in_([3]), func.date(Appointments.schedule) == datetime.now().date())).group_by(Appointments.id).having(func.min(Appointments.id)).order_by(Appointments.updated_at.desc()).all()

    def readHistory(id):
        return Appointments.query.filter(and_(Appointments.status_id.in_([1,2]), Appointments.account_id==id, func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.updated_at.desc()).limit(5).all()

    def readActive():
        return Appointments.query.filter(and_(Appointments.status_id==4, func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.id.asc()).all()

    def readUpcoming():
        return Appointments.query.filter(and_(Appointments.status_id==4, func.date(Appointments.schedule) > datetime.now().date())).order_by(Appointments.schedule.asc()).order_by(Appointments.id.asc()).all()

    def readApprovalStatus():
        return Appointments.query.filter(and_(Appointments.status_id.in_([7,8]), func.date(Appointments.schedule) > datetime.now().date())).order_by(Appointments.schedule.asc()).order_by(Appointments.id.asc()).all()

    def readDeclined():
        return Appointments.query.filter(and_(Appointments.status_id==2, func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.updated_at.desc()).limit(10).all()

    def updateAppointmentStatus(request):

        data = Appointments.query.filter_by(id=request['id']).first()
        data.status_id = request['status_id']
        db.session.commit()

        return True
    
    def updateAppointmentRemarks(request):

        data = Appointments.query.filter_by(id=request['id']).first()
        data.remarks = request['remarks']
        db.session.commit()

        return True
    
    def setAppointment(id, account_id, request):

        queues = Appointments.query.filter(Appointments.account_id==account_id, func.date(request['schedule']) == func.date(Appointments.schedule)).all()
        faculty = Accounts.query.filter_by(id=account_id).first()
        priority = str(len(queues) + 1)

        if id == "1":
            
            data = Appointments(
                priority        = priority,
                participants    = Accounts.query.filter(Accounts.id.in_(request['id_number'])).all(),
                status_id       = Status.query.filter_by(status="Pending").first().id,
                purpose_id      = request['purpose'],
                schedule        = request['schedule'],
                account_id      = account_id
            )
            db.session.add(data)
            db.session.commit()

        elif id == "2":
        
            data = Appointments(
                priority        = priority,
                participants    = Accounts.query.filter(Accounts.id.in_(request['id_number'])).all(),
                status_id       = Status.query.filter_by(status="Pending").first().id,
                purpose_id      = request['purpose'],
                schedule        = request['schedule'],
                account_id      = account_id
            )
            db.session.add(data)
            db.session.commit()

        elif id =="3":

            account = Accounts(
                first_name  = request['first_name'],
                last_name   = request['last_name'],
                status_id   = 5,
                role_id     = 4
            )
            db.session.add(account)
            db.session.commit()

            data = Appointments(
                priority        = priority,
                participants    = Accounts.query.filter(Accounts.id.in_([account.id])).all(),
                status_id       = Status.query.filter_by(status="Pending").first().id,
                purpose_id      = request['purpose'],
                schedule        = request['schedule'],
                account_id      = account_id
            )
            db.session.add(data)
            db.session.commit()
            
        return faculty.last_name.upper() + ' ' + priority

    def upsertAppointment(request):
        
        data = Appointments.query.filter_by(id=request['id']).first()

        if data == None:

            data = Appointments(
                priority        = request['priority'],
                participants    = Accounts.query.filter(Accounts.id.in_(request['participants'])).all(),
                status_id       = request['status_id'],
                remarks         = request['remarks'],
                purpose_id      = request['purpose_id'],
                schedule        = request['schedule'],
            )
            db.session.add(data)

        else:

            priority        = request['priority']
            participants    = Accounts.query.filter(Accounts.id.in_(request['participants'])).all()
            status_id       = request['status_id']
            remarks         = request['remarks']
            purpose_id      = request['purpose_id']
            schedule        = request['schedule']
                
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
