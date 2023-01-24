from flask          import flash, jsonify, render_template, request, redirect, url_for, session
from flask_login    import login_required, login_user, logout_user, current_user
from application    import app
from data.repo      import Repository
from data.schemas   import RegisterAccountSchema
from datetime       import datetime, timedelta
from functools      import wraps
import dateutil.parser as parser

# ===============================================================
# DECORATORS
# ===============================================================

@app.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    date = parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%m/%d/%Y'
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

        if current_user.role_id is None:
            return redirect(url_for('patient_dashboard'))
            
        if current_user.role_id == 3:
            return redirect(url_for('patient_dashboard'))

        return f(*args, **kwargs)
    return wrapper
       
def patient_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        if current_user.role_id == 1:
            return redirect(url_for('dashboard'))

        # if current_user.role_id == 2:
        #     return redirect(url_for('dashboard'))
            
        return f(*args, **kwargs)
    return wrapper
       

# ===============================================================
# WEB VIEWS
# ===============================================================
 
@app.route('/')
@login_required
def home():
    return redirect(url_for('dashboard'))

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
        'services'      : Repository.readServices(),
        'accounts'      : Repository.readAccounts(),
        'residents'     : Repository.readResidentAccounts(),
        'records'       : Repository.readRecords(),
        'appointments'  : Repository.readDailyAppointments(datetime.now().strftime('%m/%d/%Y')),
        'inventories'   : Repository.readInventories(),
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
            'services'      : Repository.readServices(),
            'accounts'      : Repository.readAccounts(),
            'residents'     : Repository.readResidentAccounts(),
            'records'       : Repository.readRecords(),
            'appointments'  : Repository.searchAppointments(request.form),
            'inventories'   : Repository.readInventories(),
            'current_date'  : datetime.strptime(date, '%m/%d/%Y'),
            'form'          : request.form
        }
        return render_template('admin/appointments.html', data=response)

    return redirect(url_for('appointments'))

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
        'roles' : Repository.readRoles(),
        'status' : Repository.readAllStatus()
    }
    return render_template('admin/settings.html', data=response)

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
