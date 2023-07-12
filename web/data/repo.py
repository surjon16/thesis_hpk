from data.repositories.accounts         import AccountsRepo
from data.repositories.appointments     import AppointmentsRepo
from data.repositories.consultations    import ConsultationsRepo
from data.repositories.purpose          import PurposeRepo
from data.repositories.queue            import QueuesRepo
from data.repositories.roles            import RolesRepo
from data.repositories.status           import StatusRepo

from data                               import db
from data.models                        import Roles, Status, Accounts, Purpose, Consultations

class Repository(AccountsRepo, AppointmentsRepo, ConsultationsRepo, PurposeRepo, QueuesRepo, RolesRepo, StatusRepo ):

    def __init__(self):
        pass

# =============================================================================================

    def populate():

        # db.drop_all()
        # db.create_all()

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

        status = Status(status='Done')
        db.session.add(status)

        status = Status(status='Declined')
        db.session.add(status)

        status = Status(status='Calling')
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
            first_name      = 'System',
            middle_name     = '',
            last_name       = 'Administrator',
            gender          = '',
            phone           = '+639354796747',
            birth_date      = '',
            address         = 'CDO',
            email           = 'admin@gmail.com',
            image_profile   = 'img/admin.jpg',
            password        = 'admin1234',
            role_id         = 1,
            status_id       = 6
        )
        db.session.add(account)

        # faculties
        account = Accounts(
            first_name      = 'Arlene',
            middle_name     = '',
            last_name       = 'Baldelovar',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'arlene.baldelovar@ustp.edu.ph',
            image_profile   = 'img/arlene.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Jocelyn',
            middle_name     = '',
            last_name       = 'Barbosa',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jocelyn.barbosa@ustp.edu.ph',
            image_profile   = 'img/jocelyn.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'John Benedict',
            middle_name     = '',
            last_name       = 'Bernardo',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jbl.bernardo@ustp.edu.ph',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Geraldine',
            middle_name     = '',
            last_name       = 'Blanco',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'geraldine.blanco@ustp.edu.ph',
            image_profile   = 'img/geraldine.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Petal May',
            middle_name     = '',
            last_name       = 'Dal',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'petalmay.dal@ustp.edu.ph',
            image_profile   = 'img/petalmay.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Marylene',
            middle_name     = '',
            last_name       = 'Eder',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'mseder@ustp.edu.ph',
            image_profile   = 'img/mseder.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Paul Joseph',
            middle_name     = '',
            last_name       = 'Estrera',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'paul.estrera@ustp.edu.ph',
            image_profile   = 'img/paul.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Rhea Suzette',
            middle_name     = '',
            last_name       = 'Haguisan',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'rhea.haguisan@ustp.edu.ph',
            image_profile   = 'img/rhea.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Angel',
            middle_name     = '',
            last_name       = 'Jumawan',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'angel.jumawan@ustp.edu.ph',
            image_profile   = 'img/angel.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Junar',
            middle_name     = '',
            last_name       = 'Landicho',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'junarlandicho@ustp.edu.ph',
            image_profile   = 'img/junarlandicho.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Jomar',
            middle_name     = '',
            last_name       = 'Llevado',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jomar.llevado@ustp.edu.ph',
            image_profile   = 'img/jomar.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Floreto',
            middle_name     = '',
            last_name       = 'Quinito Jr.',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jun.quinito@ustp.edu.ph',
            image_profile   = 'img/jun.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Love Jhoye',
            middle_name     = '',
            last_name       = 'Raboy',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'lovejhoye.raboy@ustp.edu.ph',
            image_profile   = 'img/lovejhoye.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Jay Noel',
            middle_name     = '',
            last_name       = 'Rojo',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jaynoel.rojo@ustp.edu.ph',
            image_profile   = 'img/jaynoel.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Jc Vanny Mill',
            middle_name     = '',
            last_name       = 'Saledaien',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jcvannymill.saledaien@ustp.edu.ph',
            image_profile   = 'img/jcvannymill.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Ulrich Lee',
            middle_name     = '',
            last_name       = 'Uy',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'ulrich.uy@ustp.edu.ph',
            image_profile   = 'img/ulrich.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Charlane',
            middle_name     = '',
            last_name       = 'Vallar',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'charlane.vallar@ustp.edu.ph',
            image_profile   = 'img/charlane.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Al-Monte Vince',
            middle_name     = '',
            last_name       = 'Calo',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'vince.calo@ustp.edu.ph',
            image_profile   = 'img/vince.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Ma. Esther',
            middle_name     = '',
            last_name       = 'Chio',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'maesther.chio@ustp.edu.ph',
            image_profile   = 'img/maesther.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Maricel',
            middle_name     = '',
            last_name       = 'Esclamado',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'maricel.esclamado@ustp.edu.ph',
            image_profile   = 'img/maricel.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Jocelyn',
            middle_name     = '',
            last_name       = 'Garrido',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'jocelyn.garrido@ustp.edu.ph',
            image_profile   = 'img/garrido.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        account = Accounts(
            first_name      = 'Archie',
            middle_name     = '',
            last_name       = 'Pachica',
            gender          = '',
            phone           = '',
            birth_date      = '',
            address         = '',
            email           = 'archie.pachica@ustp.edu.ph',
            image_profile   = 'img/archie.jpg',
            password        = 'admin1234',
            position        = 'Instructor',
            role_id         = 2,
            status_id       = 6
        )
        db.session.add(account)

        # create consultations

        consultation = Consultations(
            time_start  = '2023-02-06 15:00:00',
            time_end    = '2023-02-06 17:00:00',
            account_id  = 2,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 15:00:00',
            time_end    = '2023-02-06 17:00:00',
            account_id  = 4,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, CDO Bites'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 13:00:00',
            time_end    = '2023-02-06 15:00:00',
            account_id  = 5,
            day         = 'Monday',
            room        = 'Bldg 9 (ICT Bldg), Ground floor, CITC Dean\'s Office'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 15:00:00',
            time_end    = '2023-02-06 17:00:00',
            account_id  = 6,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 15:00:00',
            time_end    = '2023-02-06 17:00:00',
            account_id  = 7,
            day         = 'Monday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 08:00:00',
            time_end    = '2023-02-06 10:00:00',
            account_id  = 8,
            day         = 'Friday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 16:00:00',
            time_end    = '2023-02-06 18:00:00',
            account_id  = 8,
            day         = 'Tuesday',
            room        = 'Engineering Bldg, TPCO Office'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 10:00:00',
            time_end    = '2023-02-06 12:00:00',
            account_id  = 9,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 2nd floor, DTO'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 10:00:00',
            time_end    = '2023-02-06 12:00:00',
            account_id  = 10,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 10:00:00',
            time_end    = '2023-02-06 12:00:00',
            account_id  = 11,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 10:00:00',
            time_end    = '2023-02-06 12:00:00',
            account_id  = 13,
            day         = 'Thursday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 10:00:00',
            time_end    = '2023-02-06 12:00:00',
            account_id  = 14,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 09:00:00',
            time_end    = '2023-02-06 11:00:00',
            account_id  = 15,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 09:00:00',
            time_end    = '2023-02-06 11:00:00',
            account_id  = 16,
            day         = 'Wednesday',
            room        = 'Bldg 42 (Engineering Complex), 1st floor, IGIS'
        )
        db.session.add(consultation)
        
        consultation = Consultations(
            time_start  = '2023-02-06 09:00:00',
            time_end    = '2023-02-06 11:00:00',
            account_id  = 17,
            day         = 'Wednesday',
            room        = 'Bldg 9 (ICT Bldg), 4th floor, IT Faculty'
        )
        db.session.add(consultation)
        
        db.session.commit()

        return True
    
    def drop():

        db.drop_all()
        db.create_all()
    
        return True