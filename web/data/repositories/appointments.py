from data.models    import Accounts, Appointments, Status, Queue
from data           import db

from sqlalchemy     import extract, or_, and_, func
from datetime       import datetime

class AppointmentsRepo:

    def toDate(dateString): 
        return 
    
    # ==================================================================================
    # APPOINTMENTS
    
    def readAppointments():
        return Appointments.query.order_by(Appointments.status_id.desc(), Appointments.schedule.asc()).all()
    
    def searchAppointments(request):

        # if request is None:
        #     return Appointments.query.order_by(Appointments.status_id.desc(), Appointments.schedule.asc()).all()

        start_date  = request.args.get('start_date',    default = datetime.now)
        end_date    = request.args.get('end_date',      default = datetime.now)
        account     = request.args.get('account',       None)
        status      = request.args.get('status',        None)
        purpose     = request.args.get('purpose',       None)

        query = Appointments.query

        if request.args.get('start_date') == '' or request.args.get('start_date') is None:
            start_date  = end_date = datetime.now().date()
        else:
            start_date  = datetime.strptime(start_date, "%m/%d/%Y").date()
            end_date    = datetime.strptime(end_date, "%m/%d/%Y").date()

        if account is not None:
            query = query.filter_by(account_id=account)

        if status is not None:
            query = query.filter_by(status_id=status)

        if purpose is not None:
            query = query.filter_by(purpose_id=purpose)

        return query.filter(and_(func.date(Appointments.schedule) >= start_date, func.date(Appointments.schedule) <= end_date)).order_by(Appointments.updated_at.desc()).all()
    
    def readAppointment(id):
        return Appointments.query.filter_by(id=id).first()
    
    def readCall(id):
        return Appointments.query.filter(and_(Appointments.status_id==3, Appointments.account_id==id, func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.id.asc()).first()

    def readCalls():
        return Appointments.query.filter(and_(Appointments.status_id.in_([2,3]), func.date(Appointments.schedule) == datetime.now().date())).order_by(Appointments.updated_at.desc()).all()
    
    def readMonitorHeader():
        connection = db.session
        data = connection.query(Appointments).filter(Appointments.updated_at.in_(db.session.query(func.max(Appointments.updated_at)).filter(and_(Appointments.status_id.in_([1,2,3]), func.date(Appointments.schedule) == datetime.now().date())).group_by(Appointments.account_id).order_by(Appointments.updated_at.desc()).subquery())).order_by(Appointments.updated_at.desc())
        connection.remove()
        return data
    
    def readMonitorLastCall():
        connection = db.session
        data = connection.query(Queue).filter(Queue.updated_at.in_(db.session.query(func.max(Queue.updated_at)).filter(and_(func.date(Queue.schedule) == datetime.now().date())).group_by(Queue.account_id).order_by(Queue.updated_at.desc()).subquery())).order_by(Queue.updated_at.desc())
        connection.remove()
        return data
    
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

        if request['status_id'] == '3':
            
            queue = Queue(
                appointment_id     = data.id,
                schedule           = data.schedule,
                account_id         = data.account_id
            )
            db.session.add(queue)
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
