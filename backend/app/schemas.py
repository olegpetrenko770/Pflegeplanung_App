from . import ma

class PatientSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'medical_history')

class CaregiverSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'phone')

class AppointmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'patient_id', 'caregiver_id', 'date', 'notes')
