from flask import Blueprint, request, jsonify
from .models import db, Patient, Caregiver, Appointment
from .schemas import PatientSchema, CaregiverSchema, AppointmentSchema

api = Blueprint('api', __name__)

patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
caregiver_schema = CaregiverSchema()
caregivers_schema = CaregiverSchema(many=True)
appointment_schema = AppointmentSchema()
appointments_schema = AppointmentSchema(many=True)

@api.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(name=data['name'], age=data['age'], medical_history=data.get('medical_history'))
    db.session.add(new_patient)
    db.session.commit()
    return patient_schema.jsonify(new_patient), 201

@api.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    return patients_schema.jsonify(patients), 200

# Weitere Routen für Caregiver und Appointments
