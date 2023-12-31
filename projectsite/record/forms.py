# myapp/forms.py
from django.forms import ModelForm
from django import forms
from .models import Vet, Pet, Appointment, Treatment, Prescription

class VetForm(ModelForm):
    class Meta:
        model = Vet
        fields = "__all__"

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = "__all__"

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = "__all__"

class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = "__all__"
