from flask          import flash, jsonify, render_template, request, redirect, url_for, session, send_file
from flask_login    import login_required, login_user, logout_user, current_user
from application    import app
from data.repo      import Repository
from data.schemas   import RegisterAccountSchema, RegisterStudentAccountSchema
from datetime       import datetime, timedelta
from functools      import wraps
from io             import BytesIO
from werkzeug.utils import secure_filename
import dateutil.parser as parser


# ===============================================================
# DECORATORS
# ===============================================================

app.jinja_env.filters['zip'] = zip

@app.template_filter('day_of_week')
def _jinja2_filter_datetime(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%B %d, %Y'
    return native.strftime(format)

@app.template_filter('strfdate')
def _jinja2_filter_datetime(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%m/%d/%Y'
    return native.strftime(format)

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%hh:%mm %tt'
    return native.strftime(format)

@app.context_processor
def inject_now():
    return {
        'now'   : datetime.now(),
        'day'   : timedelta(days=1),
        'month' : timedelta(days=30),
        'time_schedules' : [
            {'v': 9,  't':'09:00AM-10:00AM'},
            {'v': 10, 't':'10:00AM-11:00AM'},
            {'v': 11, 't':'11:00AM-12:00NN'},
            {'v': 13, 't':'01:00PM-02:00PM'},
            {'v': 14, 't':'02:00PM-03:00PM'},
            {'v': 15, 't':'03:00PM-04:00PM'},
            {'v': 16, 't':'04:00PM-05:00PM'}
        ]
    }

def admin_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if current_user.role_id == 2:
            return redirect(url_for('faculty_dashboard'))

        if current_user.role_id == 3:
            return redirect(url_for('student_dashboard'))

        if current_user.role_id == 4 or current_user.role_id is None:
            return redirect(url_for('guest_dashboard'))

        return f(*args, **kwargs)
    return wrapper

# ===============================================================
# COMMON WEB VIEWS
# ===============================================================

@app.route('/')
def faculties():
    response = {
        'faculties'  : Repository.readFaculties()
    }
    return render_template('common/faculties.html', data=response)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = Repository.loginAccount(request.form)
        if data is not None and data is not False:
            if data.role_id is not None:
                if data.role_id < 3 :
                    return redirect(url_for('dashboard'))        
            return redirect(url_for('patient_dashboard'))
        else:
            flash('Invalid credentials.')
    return render_template('common/login.html')

@app.route('/logout')
@login_required
def logout():
    Repository.logoutAccount(current_user.id)
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        
        validator = RegisterAccountSchema(unknown='EXCLUDE')
        errors = validator.validate(request.form)

        if errors:
            return render_template('common/register.html', data={'errors': errors, 'input': request.form})

        if Repository.registerAccount(request.form):
            return redirect(url_for('login'))
        
    return render_template('common/register.html', data={'errors':[], 'input': []})

@app.route('/register_non_faculty', methods=['POST', 'GET'])
def register_non_faculty():
    if request.method == 'POST':
        
        validator = RegisterStudentAccountSchema(unknown='EXCLUDE')
        errors = validator.validate(request.form)

        if errors:
            return render_template('common/register_non_faculty.html', data={'errors': errors, 'input': request.form})

        if Repository.registerStudentAccount(request.form):
            return redirect(url_for('faculties'))
        
    return render_template('common/register_non_faculty.html', data={'errors':[], 'input': []})

@app.route('/window')
def window():
    response = {
        'faculties' : Repository.readFaculties(),
        'calls'     : Repository.readCalls(),
        'active'    : Repository.readActive(),
        'declined'  : Repository.readDeclined()
    }
    return render_template('common/window.html', data=response)

@app.route('/common/faculty/<id>')
def faculty(id):
    response = {
        'account'       : Repository.readAccount(id),
    }
    return render_template('common/faculty.html', data=response)

@app.route('/common/wave/<id>/<faculty_id>', methods=['POST', 'GET'])
def wave(id, faculty_id):

    if request.method == 'POST':
        response = Repository.setAppointment(id, faculty_id, request.form.to_dict(flat=False))
        return render_template('common/success.html', data=response)
    
    Repository.updateInquiries(faculty_id)
        
    response = {
        'purpose'   : Repository.readAllPurpose(),
        'students'  : Repository.readStudents(),
        'faculty'   : Repository.readAccount(faculty_id),
    }
    return render_template('common/wave.html', data={'errors':[], 'input': [], 'id': id, 'faculty_id': faculty_id, 'repo': response})

# @app.route('/common/wave/send', methods=['POST', 'GET'])
# def wave_send():
#     pass
#     # return render_template('common/wave.html', data={'errors':[], 'input': request.form})

# ===============================================================
# FACULTY WEB VIEWS
# ===============================================================

@app.route('/faculty/dashboard')
@login_required
def faculty_dashboard():
    response = {
        'call'      : Repository.readCall(current_user.id),
        'history'   : Repository.readHistory(current_user.id),
        'active'    : Repository.readActive()
    }
    return render_template('faculty/dashboard.html', data=response)

@app.route('/faculty/appointments')
@login_required
def faculty_upcoming():
    response = {
        'upcoming'  : Repository.readUpcoming(),
        'approval'  : Repository.readApprovalStatus(),
    }
    return render_template('faculty/appointments.html', data=response)

@app.route('/faculty/consultation')
@login_required
def faculty_consultation():
    response = {        
        'consultations' : Repository.readAccountConstultations(current_user.id),
    }
    return render_template('faculty/consultation.html', data=response)

@app.route('/faculty/profile')
@login_required
def faculty_profile():
    response = Repository.readAccount(current_user.id)
    return render_template('faculty/profile.html', data=response)

# ===============================================================
# ADMIN WEB VIEWS
# ===============================================================

@app.route('/admin/dashboard')
@login_required
@admin_login_required
def dashboard():
    response = {
        'accounts'  : Repository.readRegisteredAccounts(),
        'appointments' : Repository.readAppointments()
    }
    return render_template('admin/dashboard.html', data=response)

@app.route('/admin/appointments')
@login_required
@admin_login_required
def appointments():
    response = {
        'roles'         : Repository.readRoles(),
        'status'        : Repository.readAllStatus(),
        'accounts'      : Repository.readAccounts(),
        'appointments'  : Repository.readAppointments(),
        'current_date'  : datetime.now(),
        'form'          : None
    }
    return render_template('admin/appointments.html', data=response)

@app.route('/admin/appointment/<id>')
@login_required
@admin_login_required
def appointment(id):
    response = {
        'appointment' : Repository.readAppointment(id)
    }
    return render_template('admin/appointment.html', data=response)

@app.route('/admin/appointment/search', methods=['POST', 'GET'])
@login_required
@admin_login_required
def search_appointments():
    if request.method == 'POST':
        date = request.form['start_date']
        response = {
            'roles'         : Repository.readRoles(),
            'status'        : Repository.readAllStatus(),
            'accounts'      : Repository.readAccounts(),
            'residents'     : Repository.readResidentAccounts(),
            'appointments'  : Repository.searchAppointments(request.form),
            'current_date'  : datetime.strptime(date, '%m/%d/%Y'),
            'form'          : request.form
        }
        return render_template('admin/appointments.html', data=response)

    return redirect(url_for('appointments'))

# @app.route("/admin/table_appointments", methods=['GET'])
# @login_required
# @admin_login_required
# def table_appointments():
#     response = {
#         'appointments'  : Repository.readAppointments(),
#         'current_date'  : datetime.now(),
#     }
#     return render_template('admin/table_appointments.html', data=response)

# @app.route("/admin/export_to_excel", methods=['GET'])
# @login_required
# @admin_login_required
# def export_to_excel():

#     #create a random Pandas dataframe
#     df_1 = pd.read_html(url_for('table_appointments'))

#     #create an output stream
#     output = BytesIO()
#     writer = pd.ExcelWriter(output, engine='xlsxwriter')

#     #taken from the original question
#     df_1.to_excel(writer, startrow = 0, merge_cells = False, sheet_name = "Sheet_1")
#     workbook = writer.book
#     worksheet = writer.sheets["Sheet_1"]
#     format = workbook.add_format()
#     format.set_bg_color('#eeeeee')
#     worksheet.set_column(0,9,28)

#     #the writer has done its job
#     writer.close()

#     #go back to the beginning of the stream
#     output.seek(0)

#     #finally return the file
#     return send_file(output, attachment_filename="testing.xlsx", as_attachment=True)

@app.route('/admin/accounts')
@login_required
@admin_login_required
def accounts():
    response = Repository.readAccounts()
    return render_template('admin/accounts.html', data=response)

@app.route('/admin/account/<id>')
@login_required
@admin_login_required
def account(id):
    response = Repository.readAccount(id)
    return render_template('admin/account.html', data=response)

@app.route('/admin/settings')
@login_required
@admin_login_required
def settings():
    response = {
        'purpose'   : Repository.readAllPurpose(),
        'roles'     : Repository.readRoles(),
        'status'    : Repository.readAllStatus()
    }
    return render_template('admin/settings.html', data=response)

# ====================================================================================

def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route('/uploader', methods = ['POST'])
def uploader_file():
    
    f = request.files['file']
    filename = 'img/'+secure_filename(f.filename)
    f.save('/home/server/thesis_hpk/web/application/static/'+filename)
    Repository.updatePhoto(request.form, filename)

    return redirect(redirect_url())
