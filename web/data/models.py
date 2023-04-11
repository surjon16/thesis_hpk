import json
from data                   import db
from data                   import login_manager
from flask_login            import UserMixin
from sqlalchemy.ext.hybrid  import hybrid_property, hybrid_method
from sqlalchemy             import select, func
from werkzeug.security      import generate_password_hash, check_password_hash

participants = db.Table('participants',
    db.Column('participant_id', db.Integer, db.ForeignKey('accounts.id'), primary_key=True),
    db.Column('appointment_id', db.Integer, db.ForeignKey('appointments.id'), primary_key=True)
)

class Accounts(UserMixin, db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    id_number   = db.Column(db.String(20))
    first_name  = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name   = db.Column(db.String(100))
    gender      = db.Column(db.String(10))
    phone       = db.Column(db.String(15))
    birth_date  = db.Column(db.DateTime)
    address     = db.Column(db.String(100))
    # position    = db.Column(db.String(100))
    # objective   = db.Column(db.String(100))

    # login
    email           = db.Column(db.String(100))
    password_hash   = db.Column(db.String(128))

    # images
    image_profile   = db.Column(db.String(128), default="img/no-photo.jpg")
    image_location  = db.Column(db.String(128), default="img/no-photo.jpg")

    # timestamps
    login_date  = db.Column(db.DateTime, default=db.func.current_timestamp())
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship
    role_id         = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=True)
    status_id       = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=True)
    participant     = db.relationship('Appointments', secondary=participants, backref=db.backref('participant', uselist=False),  lazy='dynamic')
    consultations   = db.relationship('Consultations', backref='faculty', lazy=True)
    faculty         = db.relationship('Appointments', backref='faculty', lazy=True)


    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        return {
            'id'            : self.id,
            'id_number'     : self.id_number,
            'first_name'    : self.first_name,
            'middle_name'   : self.middle_name,
            'last_name'     : self.last_name,
            'gender'        : self.gender,
            'phone'         : self.phone,
            'birth_date'    : self.birth_date.strftime('%m/%d/%Y') if self.birth_date is not None else None,
            'email'         : self.email,
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at,
            'address'       : self.address,
            'role_id'       : self.role_id,
            'role'          : self.role.role,
            'status_id'     : self.status_id,
            'profile'       : self.image_profile,
            'location'      : self.image_location,
            'status'        : self.status.status
        }

class Consultations(db.Model):
    
    # consultation info
    id          = db.Column(db.Integer, primary_key=True)
    time_start  = db.Column(db.DateTime)
    time_end    = db.Column(db.DateTime)
    day         = db.Column(db.String(10))
    room        = db.Column(db.String(100))

    # timestamps
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship
    account_id  = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=True)
    
    @hybrid_property
    def schedule(self):
        return {
            'day': self.day, 
            'time': self.time_start.strftime('%I:%M%p') + ' - ' + self.time_end.strftime('%I:%M%p'),
        }
    
    def serialize(self):
        return {
            'id'            : self.id,
            'schedule'      : self.schedule,
            'time_start'    : self.time_start.strftime('%H:%M'),
            'time_end'      : self.time_end.strftime('%H:%M'),
            'day'           : self.day,
            'room'          : self.room,
            'faculty'       : self.faculty.first_name + ' ' + self.faculty.middle_name + ' ' + self.faculty.last_name,

        }

class Appointments(db.Model):

    # appointment info
    id          = db.Column(db.Integer, primary_key=True)
    priority    = db.Column(db.String(15))
    remarks     = db.Column(db.String(100))
    schedule    = db.Column(db.DateTime, default=db.func.current_timestamp())

    # timestamps
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship
    purpose_id      = db.Column(db.Integer, db.ForeignKey('purpose.id'), nullable=True)
    status_id       = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=True)
    account_id      = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=True)
    participants    = db.relationship('Accounts', secondary=participants, lazy='subquery', backref=db.backref('appointment', lazy=True))
    
    @hybrid_property
    def participants_list(self): 
        return None if self.participants is None else self.participants
    
    def serialize(self):
        return {
            'id'            : self.id,
            'purpose'       : self.purpose.purpose,
            'priority'      : self.priority,
            'faculty'       : self.account_id,
            'faculty_name'  : self.faculty.last_name.upper(),
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at,
            'status'        : self.status.status,
        }

class Queue(db.Model):

    # appointment info
    id              = db.Column(db.Integer, primary_key=True)
    priority        = db.Column(db.String(15))

    # timestamps
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def serialize(self):
        return {
            'id'            : self.id,
            'priority'      : self.priority,
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at,
        }

class Purpose(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    purpose = db.Column(db.String(50))

    # timestamps
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship
    appointment_purpose  = db.relationship('Appointments', backref='purpose', lazy=True)

    def serialize(self):
        return {
            'id'            : self.id,
            'purpose'       : self.purpose,
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at
        }

class Roles(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    role    = db.Column(db.String(20))

    # timestamps
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship
    accounts_roles = db.relationship('Accounts', backref='role', lazy=True)

    def serialize(self):
        return {
            'id'            : self.id,
            'role'          : self.role,
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at
        }
  
class Status(db.Model):

    id      = db.Column(db.Integer, primary_key=True)
    status  = db.Column(db.String(50))

    # timestamps
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # relationship
    appointment_status  = db.relationship('Appointments',   backref='status', lazy=True)
    accounts_status     = db.relationship('Accounts', backref='status', lazy=True)

    def serialize(self):
        return {
            'id'            : self.id,
            'status'        : self.status,
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at
        }

# ============================================================================================
@login_manager.user_loader
def load_user(id):
    return Accounts.query.get(int(id))
