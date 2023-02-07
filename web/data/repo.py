from data.repositories.accounts         import AccountsRepo
from data.repositories.appointments     import AppointmentsRepo
from data.repositories.consultations    import ConsultationsRepo
from data.repositories.roles            import RolesRepo
from data.repositories.status           import StatusRepo
from data.repositories.purpose          import PurposeRepo

from data                               import db
from data.models                        import Roles, Status, Accounts, Purpose, Consultations, Appointments

class Repository(AccountsRepo, AppointmentsRepo, ConsultationsRepo, RolesRepo, StatusRepo, PurposeRepo):

    def __init__(self):
        pass

# =============================================================================================

    def populate():

        # create roles

        role = Roles(role='admin')
        db.session.add(role)

        role = Roles(role='faculty')
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

        status = Status(status='Unavailable')
        db.session.add(status)

        status = Status(status='Fullybooked')
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
            last_name   = 'Faculty',
            gender      = '',
            phone       = '+639354796747',
            birth_date  = '',
            address     = 'CDO',
            email       = 'faculty@gmail.com',
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

        # create consultations

        consultation = Consultations(
            time_start  = '2023-02-06 13:00:00',
            time_end    = '2023-02-06 13:30:00',
            account_id  = Accounts.query.filter_by(role_id=2).first().id,
            day         = 'Monday'
        )
        db.session.add(consultation)

        # create appointments

        appointment = Appointments(
            time_start      = Consultations.query.filter_by(id=1).first().time_start,
            time_end        = Consultations.query.filter_by(id=1).first().time_end,
            priority        = Accounts.query.filter_by(role_id=2).first().last_name + str(Appointments.query.count() + 1),
            participants    = Accounts.query.filter(Accounts.id.in_([2,3])).all(),
            status_id       = Status.query.filter_by(status="Pending").first().id,
            purpose_id      = Purpose.query.filter_by(purpose="Capstone").first().id
        )
        db.session.add(appointment)

        appointment = Appointments(
            time_start      = Consultations.query.filter_by(id=1).first().time_start,
            time_end        = Consultations.query.filter_by(id=1).first().time_end,
            priority        = Accounts.query.filter_by(role_id=2).first().last_name + str(Appointments.query.count() + 1),
            participants    = Accounts.query.filter(Accounts.id.in_([2,4])).all(),
            status_id       = Status.query.filter_by(status="Pending").first().id,
            purpose_id      = Purpose.query.filter_by(purpose="Inquire").first().id
        )
        db.session.add(appointment)

        # create queueing

        

        db.session.commit()

        return True    