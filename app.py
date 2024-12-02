from flask import Flask, render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from database import db_session
from models import Patient, Doctor, Appointment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqbpro'


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
        firstname = request.form['firstname']
        patrname = request.form['patrname']
        spec = request.form['spec']
        cab = int(request.form['cab'])
        new_doctor = Doctor(lastname=lastname, firstname=firstname,
                            patrname=patrname, spec=spec, cab=cab)
        db_session.add(new_doctor)
        db_session.commit()
        return redirect('/doctors')

    else:
        return render_template('doctors-edit.html')


@app.route('/patients')
def patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)


@app.route('/patients-edit', methods=['POST', 'GET'])
def patients_edit():
    if request.method == 'POST':
        lastname = request.form['lastname']
        firstname = request.form['firstname']
        patrname = request.form['patrname']
        oms = request.form['oms']
        birthday = request.form['birthday']
        sex = request.form['sex']
        adress = request.form['adress']
        phone = request.form['phone']
        new_patient = Patient(lastname=lastname, firstname=firstname,
                              patrname=patrname, oms=oms, birthday=birthday,
                              sex=sex, adress=adress, phone=phone)
        db_session.add(new_patient)
        db_session.commit()
        return redirect('/patients')

    else:
        return render_template('patients-edit.html')


@app.route('/appointments/delete_record', methods=['POST', 'GET'])
def appoint_delete_record():
    record_id = int(request.form['record_id'])
    record = Appointment.query.filter_by(id=record_id).first()
    if record is None:
        abort(404)
    db_session.delete(record)
    db_session.commit()
    statement = f'Запись с id = {record_id} удалена успешно'
    return render_template('status.html', statement=statement)


@app.route('/doctors/delete_record', methods=['POST', 'GET'])
def doctors_delete_record():
    record_id = int(request.form['record_id'])
    record = Doctor.query.filter_by(id=record_id).first()
    if record is None:
        abort(404)
    db_session.delete(record)
    db_session.commit()
    statement = f'Запись с id = {record_id} удалена успешно'
    return render_template('status.html', statement=statement)


@app.route('/patients/delete_record', methods=['POST', 'GET'])
def patients_delete_record():
    record_id = int(request.form['record_id'])
    record = Patient.query.filter_by(id=record_id).first()
    if record is None:
        abort(404)
    db_session.delete(record)
    db_session.commit()
    statement = f'Запись с id = {record_id} удалена успешно'
    return render_template('status.html', statement=statement)


if __name__ == '__main__':
    app.run(debug=True)
