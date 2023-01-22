from data.repositories.accounts         import AccountsRepo
from data.repositories.appointments     import AppointmentsRepo
from data.repositories.roles            import RolesRepo
from data.repositories.status           import StatusRepo
from data.repositories.purpose          import PurposeRepo

from data                               import db
from data.models                        import Roles, Status, Accounts, Purpose

class Repository(AccountsRepo, AppointmentsRepo, RolesRepo, StatusRepo, PurposeRepo):

    def __init__(self):
        pass

# =============================================================================================

    def populate():

        # create roles

        role = Roles(role='admin')
        db.session.add(role)

        role = Roles(role='instructor')
        db.session.add(role)

        role = Roles(role='student')
        db.session.add(role)

        role = Roles(role='guest')
        db.session.add(role)

        # create purpose

        purpose = Purpose(purpose='Inquire')
        db.session.add(purpose)

        purpose = Purpose(purpose='Grades')
        db.session.add(purpose)

        purpose = Purpose(purpose='Assignment')
        db.session.add(purpose)

        purpose = Purpose(purpose='Activity')
        db.session.add(purpose)

        purpose = Purpose(purpose='Project')
        db.session.add(purpose)

        purpose = Purpose(purpose='Capstone')
        db.session.add(purpose)

        # create status

        status = Status(status='Approved')
        db.session.add(status)

        status = Status(status='Declined')
        db.session.add(status)

        status = Status(status='Cancelled')
        db.session.add(status)

        status = Status(status='Pending')
        db.session.add(status)

        status = Status(status='Available')
        db.session.add(status)

        # create accounts

        account = Accounts(
            first_name  = 'System',
            middle_name = '',
            last_name   = 'Administrator',
            gender      = '',
            phone       = '+639354796747',
            birth_date  = '',
            address     = 'CDO',
            email       = 'admin@gmail.com',
            password    = 'admin1234',
            role_id     = 1
        )
        db.session.add(account)

        account = Accounts(
            first_name  = 'Sample',
            middle_name = '',
            last_name   = 'Instructor',
            gender      = '',
            phone       = '+639354796747',
            birth_date  = '',
            address     = 'CDO',
            email       = 'instructor@gmail.com',
            password    = 'admin1234',
            role_id     = 2
        )
        db.session.add(account)

        account = Accounts(
            first_name  = 'Sample',
            middle_name = '',
            last_name   = 'Student',
            gender      = '',
            phone       = '+639354796747',
            birth_date  = '',
            address     = 'CDO',
            email       = 'student@gmail.com',
            password    = 'admin1234',
            role_id     = 3
        )
        db.session.add(account)

        account = Accounts(
            first_name  = 'Sample',
            middle_name = '',
            last_name   = 'Guest',
            gender      = '',
            phone       = '+639354796747',
            birth_date  = '',
            address     = 'CDO',
            email       = 'guest@gmail.com',
            password    = 'admin1234',
            role_id     = 4
        )
        db.session.add(account)

        db.session.commit()

        return True    