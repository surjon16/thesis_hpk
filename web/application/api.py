from flask          import jsonify, render_template, request, redirect, url_for, make_response
from application    import app
from data.repo      import Repository
from data.schemas   import CreateStudentAccountSchema, UpdateStudentAccountSchema, CreateAccountSchema, UpdateAccountSchema, CreateConsultationSchema, CreateAppointmentSchema
from data           import auth
import json

# API RESOURCE PATTERN

# GET         /data/get/<id>    get data data by id
# GET         /data/get/all     get data list
# POST        /data/upsert/     upsert data
# POST        /data/delete/     delete data

@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'hpk' and password == 'hpk':
            return True
        else:
            return False
            
# ==================================================================================
# ACCOUNTS

@app.route('/api/account/get/<id>', methods=['GET'])
def get_account(id):
    return jsonify(Repository.readAccount(id).serialize())

@app.route('/api/account/get/consultation_status/<id>', methods=['GET'])
def get_account_consultation_status(id):
    return jsonify({
        'status'        : Repository.getAccountStatus(id),
        'consultations' : [data.serialize() for data in Repository.readAccountConstultations(id)]
    })
    # return jsonify([data.serialize() for data in Repository.readAccountConstultations(id)])

@app.route('/api/account/get/consultations/<id>', methods=['GET'])
def get_account_consultations(id):
    return jsonify([data.serialize() for data in Repository.readAccountConstultations(id)])

@app.route('/api/account/get/all', methods=['GET'])
def get_all_accounts():
    return jsonify([data.serialize() for data in Repository.readAccounts()])

@app.route('/api/account/upsert', methods=['POST'])
def upsert_account():


    if int(request.form['id']) == -1:

        validator = CreateStudentAccountSchema(unknown='EXCLUDE') if int(request.form['role_id']) == 3 else  CreateAccountSchema(unknown='EXCLUDE')

        errors = validator.validate(request.form)
        if errors:
            return jsonify({'success':False, 'errors':errors})

    else:

        validator = UpdateStudentAccountSchema(unknown='EXCLUDE') if int(request.form['role_id']) == 3 else UpdateAccountSchema(unknown='EXCLUDE')

        errors = validator.validate(request.form)
        if errors:
            return jsonify({'success':False, 'errors':errors})

    data = Repository.upsertAccount(request.form)

    if data:
        return {'success':True , 'account': Repository.readAccount(data.id).serialize()}

    return {'success':False}

@app.route('/api/account/delete', methods=['POST'])
def delete_account():
    if Repository.deleteAccount(request.form):
        return {'success':True}
    return {'success':False}

@app.route('/api/account/get/status/<id>', methods=['GET'])
def get_account_status(id):
    return jsonify(Repository.getAccountStatus(id))

@app.route('/api/account/update/status', methods=['POST'])
def update_account_status():
    if Repository.updateAccountStatus(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# APPOINTMENTS

@app.route('/api/appointment/get/<id>', methods=['GET'])
def get_appointment(id):
    return jsonify(Repository.readAppointment(id).serialize())

@app.route('/api/appointment/get/all', methods=['GET'])
def get_all_appointments():
    return jsonify([data.serialize() for data in Repository.readAppointments()])

@app.route('/api/appointment/get/window_data', methods=['GET'])
def get_window_data():
    return jsonify({
        'header'    : Repository.readMonitorHeader().serialize(),
        'last_call' : [data.serialize() for data in Repository.readMonitorLastCall()],
        'declined'  : [data.serialize() for data in Repository.readDeclined()]
    })

@app.route('/api/appointment/update/status', methods=['POST'])
def update_appointment_status():    
    return {'success': Repository.updateAppointmentStatus(request.form)}

@app.route('/api/appointment/update/remarks', methods=['POST'])
def update_appointment_remarks():    
    return {'success': Repository.updateAppointmentRemarks(request.form)}

@app.route('/api/appointment/get/queue', methods=['GET'])
def get_queue():
    return jsonify({
        'active'    : [data.serialize() for data in Repository.readActive()],
        'declined'  : [data.serialize() for data in Repository.readDeclined()]
    })

@app.route('/api/appointment/upsert', methods=['POST'])
def upsert_appointment():
    
    validator = CreateAppointmentSchema(unknown='EXCLUDE')
    errors = validator.validate(request.form)

    if errors:
        return jsonify({'success':False, 'errors':errors})

    if Repository.upsertAppointment(request.form):
        return {'success':True}
    return {'success':False}

@app.route('/api/appointment/delete', methods=['POST'])
def delete_appointment():
    if Repository.deleteAppointment(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# QUEUES

@app.route('/api/queue/get/all', methods=['GET'])
def get_all_queues():
    return jsonify([data.serialize() for data in Repository.readQueue()])

@app.route('/api/queue/insert', methods=['POST'])
def insertQueue():
    if Repository.insertQueue(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# CONSULTATIONS

@app.route('/api/consultation/get/<id>', methods=['GET'])
def get_consultation(id):
    return jsonify(Repository.readConsultation(id).serialize())

@app.route('/api/consultation/get/all', methods=['GET'])
def get_all_consultations():
    return jsonify([data.serialize() for data in Repository.readConsultations()])

@app.route('/api/consultation/upsert', methods=['POST'])
def upsert_consultation():
    
    validator = CreateConsultationSchema(unknown='EXCLUDE')
    errors = validator.validate(request.form)

    if errors:
        return jsonify({'success':False, 'errors':errors})

    if Repository.upsertConsultation(request.form):
        return {'success':True}
    return {'success':False}

@app.route('/api/consultation/delete', methods=['POST'])
def delete_consultation():
    if Repository.deleteConsultation(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# PURPOSE

@app.route('/api/purpose/get/<id>', methods=['GET'])
def get_purpose(id):
    return jsonify(Repository.readPurpose(id).serialize())

@app.route('/api/purpose/get/all', methods=['GET'])
def get_all_purposes():
    return jsonify([data.serialize() for data in Repository.readPurpose()])

@app.route('/api/purpose/upsert', methods=['POST'])
def upsert_purpose():
    if Repository.upsertPurpose(request.form):
        return {'success':True}
    return {'success':False}

@app.route('/api/purpose/delete', methods=['POST'])
def delete_purpose():
    if Repository.deletePurpose(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# ROLES

@app.route('/api/role/get/<id>', methods=['GET'])
def get_role(id):
    return jsonify(Repository.readRole(id).serialize())

@app.route('/api/role/get/all', methods=['GET'])
def get_all_roles():
    return jsonify([data.serialize() for data in Repository.readRoles()])

@app.route('/api/role/upsert', methods=['POST'])
def upsert_role():
    if Repository.upsertRole(request.form):
        return {'success':True}
    return {'success':False}

@app.route('/api/role/delete', methods=['POST'])
def delete_role():
    if Repository.deleteRole(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# STATUS

@app.route('/api/status/get/<id>', methods=['GET'])
def get_status(id):
    return jsonify(Repository.readStatus(id).serialize())

@app.route('/api/status/get/all', methods=['GET'])
def get_all_status():
    return jsonify([data.serialize() for data in Repository.readAllStatus()])

@app.route('/api/status/upsert', methods=['POST'])
def upsert_status():
    if Repository.upsertStatus(request.form):
        return {'success':True}
    return {'success':False}

@app.route('/api/status/delete', methods=['POST'])
def delete_status():
    if Repository.deleteStatus(request.form):
        return {'success':True}
    return {'success':False}

# ==================================================================================
# FACTORY

@app.route('/api/populate', methods=['GET'])
def populate():
    return {'success': Repository.populate()}

@app.route('/api/drop', methods=['GET'])
def drop():
    return {'success': Repository.drop()}
