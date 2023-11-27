from data.models    import Accounts, Roles, Appointments, Status
from data           import db

from flask_login    import login_user, current_user
from sqlalchemy     import extract, or_, and_, func
from sqlalchemy.sql import label
from datetime       import datetime

class AccountsRepo:
    # ==================================================================================
    # ACCOUNTS

    def loginAccount(request):
        data = Accounts.query.filter_by(email=request['email']).first()
        if data is not None and data.verify_password(request['password']):
            login_user(data)
            return data
        else:
            return False

    def logoutAccount(id):
        data = Accounts.query.filter_by(id=id).first()
        data.status_id = 6
        db.session.commit()
        return True

    def readAccounts():
        return Accounts.query.all()

    def readFaculties():
        return Accounts.query.filter(Accounts.role_id.in_([2])).all()

    def readStudents():
        return Accounts.query.filter(Accounts.role_id.in_([3])).all()

    def readRegisteredAccounts():
        return Accounts.query.filter(Accounts.role_id.in_([1,2,3,4])).all()
    
    def readAccount(id):
        return Accounts.query.filter_by(id=id).first()

    def registerAccount(request):
        
        data = Accounts(
            first_name  = request['first_name'],
            last_name   = request['last_name'],
            phone       = request['phone'],
            email       = request['email'],
            password    = request['password'],
            status_id   = 5,
            role_id     = 2
        )

        db.session.add(data)
        db.session.commit()

        return True
    
    def registerStudentAccount(request):
        
        data = Accounts(
            id_number   = request['id_number'],
            first_name  = request['first_name'],
            last_name   = request['last_name'],
            phone       = request['phone'],
            email       = request['email'],
            password    = request['password'],
            status_id   = 5,
            role_id     = 3
        )

        db.session.add(data)
        db.session.commit()

        return True
    
    def getAccountStatus(id):
        data = Accounts.query.filter_by(id=id).first()
        if data.status_id == 5:
            return True
        return False

    def updateAccountStatus(request):
        data = Accounts.query.filter_by(id=request['id']).first()
        data.status_id = request['status_id']
        db.session.commit()
        return True

    def updatePhoto(request, file):
        
        data = Accounts.query.filter_by(id=request['photo']).first()
        if request['target'] == "1":
            data.image_profile = file
            db.session.commit()
        
        if request['target'] == "2":
            data.image_location = file
            db.session.commit()
        
        return data
        
    def updateInquiries(id):
        
        data = Accounts.query.filter_by(id=id).first()
        if data.inquiries is None: data.inquiries = 1
        else: data.inquiries += 1

        db.session.commit()
        
        return data
        
    def upsertAccount(request):

        data = Accounts.query.filter_by(id=request['id']).first()

        birth_date = request['birth_date']
        try:
            birth_date = datetime.strptime(birth_date, '%m/%d/%Y').strftime('%Y-%m-%d')
        except ValueError:
            birth_date = None

        if data == None:

            if request['password']:
                data = Accounts(
                    id_number   = request['id_number'],
                    first_name  = request['first_name'],
                    middle_name = request['middle_name'],
                    last_name   = request['last_name'],
                    gender      = request['gender'],
                    phone       = request['phone'],
                    birth_date  = birth_date,
                    address     = request['address'],
                    position    = request['position'],
                    objective   = request['objective'],
                    email       = request['email'],
                    password    = request['password'],
                    role_id     = int(request['role_id']),
                    status_id   = 5
                )
            else:
                data = Accounts(
                    id_number   = request['id_number'],
                    first_name  = request['first_name'],
                    middle_name = request['middle_name'],
                    last_name   = request['last_name'],
                    gender      = request['gender'],
                    phone       = request['phone'],
                    birth_date  = birth_date,
                    address     = request['address'],
                    position    = request['position'],
                    objective   = request['objective'],
                    email       = request['email'],
                    role_id     = int(request['role_id']),
                    status_id   = 5
                )

            try: 
                
                db.session.add(data) 
                db.session.commit() 

                return data

            except AssertionError as exception_message: 
                return None
                
        else:

            data.id_number   = request['id_number']
            data.first_name  = request['first_name']
            data.middle_name = request['middle_name']
            data.last_name   = request['last_name']
            data.gender      = request['gender']
            data.phone       = request['phone']
            data.birth_date  = birth_date
            data.address     = request['address']
            data.position    = request['position']
            data.objective   = request['objective']
            data.email       = request['email']
            data.role_id     = int(request['role_id'])

            if request['password']:
                data.password = request['password']

            db.session.commit()

        return data

    def deleteAccount(request):

        data = Accounts.query.filter_by(id=request['id']).first()
        
        if data == None:
            return False
        else:

            # # delete all notifications
            # for notification in data.account_notifications:
            #     db.session.delete(notification)

            # for appointment in data.account_appointments:
            #     db.session.delete(appointments)

            # finally, delete account
            db.session.delete(data)
            db.session.commit()

            return True
