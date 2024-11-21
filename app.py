from flask import Flask, render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from database import db_session
from models import Patient, Doctor, Appointment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

db = SQLAlchemy(app)

@app.route('/')
@app.route('/appointments')
def appointments():
    appointments = Appointment.query.all()
    return render_template('appointments.html', appointments=appointments)

@app.route('/appointments-edit', methods=['POST', 'GET'])
def appointments_edit():
    if request.method == 'POST':
        appdate = request.form['appdate']
        apptime = request.form['apptime']
        problem = request.form['problem']
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        new_appoint = Appointment(appdate=appdate, apptime=apptime,
                                  problem=problem, patient_id=patient_id,
                                  doctor_id=doctor_id)
        db_session.add(new_appoint)
        db_session.commit()
        return redirect('/appointments')
    else:
        return render_template('appointments-edit.html')

@app.route('/doctors')
def doctors():
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors)

@app.route('/doctors-edit', methods=['POST', 'GET'])
def doctors_edit():
    if request.method == 'POST':
        lastname = request.form['lastname']
        # Добавьте подходящий код для обработки других полей
        return redirect('/doctors')

if __name__ == '__main__':
    app.run(debug=True)
