from application import app
from data import db

app.secret_key = 'hi_prof_kiosk'
app.WTF_CSRF_ENABLED = True

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True, host='127.0.0.1', port='8080')
