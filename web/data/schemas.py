from datetime import datetime
from marshmallow import Schema, fields, validates, validates_schema, ValidationError

# All classes declared will be used for validation

class CreateStudentAccountSchema(Schema):
    
    id_number   = fields.Str(required=True)
    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    phone       = fields.Str(required=True)
    email       = fields.Email(required=True)
    address     = fields.Str(required=True)
    password    = fields.Str(required=True)

    @validates('id_number')
    def validate_id_number(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your id number.')

    @validates('first_name')
    def validate_first_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your first name.')

    @validates('last_name')
    def validate_last_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your last name.')

    @validates('password')
    def validate_password(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a password.')

class UpdateStudentAccountSchema(Schema):
    
    id_number   = fields.Str(required=True)
    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    phone       = fields.Str(required=True)
    email       = fields.Email(required=True)
    address     = fields.Str(required=True)
    role_id     = fields.Str(required=True)

    @validates('id_number')
    def validate_id_number(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your id number.')

    @validates('first_name')
    def validate_first_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your first name.')

    @validates('last_name')
    def validate_last_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your last name.')

    @validates('role_id')
    def validate_role_id(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a role.')

class RegisterStudentAccountSchema(Schema):

    id_number   = fields.Str(required=True)
    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    email       = fields.Email(required=True)
    phone       = fields.Str(required=True)
    password    = fields.Str(required=True)

    @validates('id_number')
    def validate_id_number(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your id number.')

    @validates('first_name')
    def validate_first_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your first name.')

    @validates('last_name')
    def validate_last_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your last name.')

    @validates('password')
    def validate_password(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a password.')

class CreateAccountSchema(Schema):
    
    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    phone       = fields.Str(required=True)
    email       = fields.Email(required=True)
    address     = fields.Str(required=True)
    password    = fields.Str(required=True)

    @validates('first_name')
    def validate_first_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your first name.')

    @validates('last_name')
    def validate_last_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your last name.')

    @validates('password')
    def validate_password(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a password.')

class UpdateAccountSchema(Schema):
    
    id_number   = fields.Str(required=True)
    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    phone       = fields.Str(required=True)
    email       = fields.Email(required=True)
    address     = fields.Str(required=True)
    role_id     = fields.Str(required=True)

    @validates('first_name')
    def validate_first_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your first name.')

    @validates('last_name')
    def validate_last_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your last name.')

    @validates('phone')
    def validate_phone(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a phone number.')
        if len(value) != 11:
            raise ValidationError('Invalid phone number.')

    @validates('address')
    def validate_address(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide an address.')

    @validates('role_id')
    def validate_role_id(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a role.')

class RegisterAccountSchema(Schema):

    first_name  = fields.Str(required=True)
    last_name   = fields.Str(required=True)
    email       = fields.Email(required=True)
    phone       = fields.Str(required=True)
    password    = fields.Str(required=True)

    @validates('first_name')
    def validate_first_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your first name.')

    @validates('last_name')
    def validate_last_name(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide your last name.')

    @validates('password')
    def validate_password(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide a password.')

class CreateAppointmentSchema(Schema):
    
    details             = fields.Str(required=True)
    appointment_date    = fields.Str(required=True)
    account_id          = fields.Str(required=True)
    status_id           = fields.Str(required=True)
    service_id          = fields.Str(required=True)
    
    @validates('details')
    def validate_details(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide details.')

    @validates('appointment_date')
    def validate_appointment_date(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide an appointment.')

    @validates('account_id')
    def validate_account_id(self, value):
        if value == '' or value is None:
            raise ValidationError('Please select an account for this appointment.')

    @validates('status_id')
    def validate_status_id(self, value):
        if value == '' or value is None:
            raise ValidationError('Please select a status.')

class CreateConsultationSchema(Schema):
    
    time_start  = fields.Str(required=True)
    time_end    = fields.Str(required=True)
    day         = fields.Str(required=True)
    faculty     = fields.Str(required=True)
    
    @validates('time_start')
    def validate_time_start(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide the start time.')

    @validates('time_end')
    def validate_time_end(self, value):
        if value == '' or value is None:
            raise ValidationError('Please provide the time it ends.')

    @validates('day')
    def validate_day(self, value):
        if value == '' or value is None:
            raise ValidationError('Please select a day for this consultation.')

    @validates('faculty')
    def validate_faculty(self, value):
        if value == '' or value is None:
            raise ValidationError('Please specify which faculty to set this schedule.')
