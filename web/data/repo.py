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

        status = Status(status='Approved')
        db.session.add(status)

        status = Status(status='Disapproved')
        db.session.add(status)

        # create accounts

        account = Accounts(
            first_name      = 'System',
            middle_name     = '',
            last_name       = 'Administrator',
            gender          = '',
            phone           = '+639354796747',
            address         = 'CDO',
            email           = 'admin@gmail.com',
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
            address         = '',
            email           = 'arlene.baldelovar@ustp.edu.ph',
            image_profile   = 'img/arlene.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jocelyn.barbosa@ustp.edu.ph',
            image_profile   = 'img/jocelyn.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jbl.bernardo@ustp.edu.ph',
            image_profile   = 'img/jbl.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'geraldine.blanco@ustp.edu.ph',
            image_profile   = 'img/geraldine.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'petalmay.dal@ustp.edu.ph',
            image_profile   = 'img/petalmay.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'mseder@ustp.edu.ph',
            image_profile   = 'img/mseder.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'paul.estrera@ustp.edu.ph',
            image_profile   = 'img/paul.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'rhea.haguisan@ustp.edu.ph',
            image_profile   = 'img/rhea.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'angel.jumawan@ustp.edu.ph',
            image_profile   = 'img/angel.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'junarlandicho@ustp.edu.ph',
            image_profile   = 'img/junarlandicho.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jomar.llevado@ustp.edu.ph',
            image_profile   = 'img/jomar.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jun.quinito@ustp.edu.ph',
            image_profile   = 'img/jun.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'lovejhoye.raboy@ustp.edu.ph',
            image_profile   = 'img/lovejhoye.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jaynoel.rojo@ustp.edu.ph',
            image_profile   = 'img/jaynoel.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jcvannymill.saledaien@ustp.edu.ph',
            image_profile   = 'img/jcvannymill.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'ulrich.uy@ustp.edu.ph',
            image_profile   = 'img/ulrich.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'charlane.vallar@ustp.edu.ph',
            image_profile   = 'img/charlane.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'vince.calo@ustp.edu.ph',
            image_profile   = 'img/vince.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'maesther.chio@ustp.edu.ph',
            image_profile   = 'img/maesther.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'maricel.esclamado@ustp.edu.ph',
            image_profile   = 'img/maricel.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'jocelyn.garrido@ustp.edu.ph',
            image_profile   = 'img/garrido.jpg',
            image_location  = 'img/no-photo.jpg',
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
            address         = '',
            email           = 'archie.pachica@ustp.edu.ph',
            image_profile   = 'img/archie.jpg',
            image_location  = 'img/no-photo.jpg',
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