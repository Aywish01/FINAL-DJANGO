from django.contrib import admin
from .models import Vet, Pet, Appointment, Treatment, Prescription

@admin.register(Vet)
class VetAdmin(admin.ModelAdmin):
    list_display = ("FirstName", "LastName", "Email", "ClinicName", "created_at", "updated_at")
    search_fields = ("FirstName", "LastName", "Email", "ClinicName")

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("PetName", "Species", "Breed", "BirthDate", "Owner", "created_at", "updated_at")
    search_fields = ("PetName", "Species", "Breed", "Owner__FirstName", "Owner__LastName", "Owner__Email")

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("PetID", "AppointmentDate", "Purpose", "created_at", "updated_at")
    search_fields = ("PetID__PetName", "Purpose")

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ("TreatmentName", "Description", "PetID", "created_at", "updated_at")
    search_fields = ("TreatmentName", "PetID__PetName")

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("MedicationName", "Dosage", "VetID", "PetID", "created_at", "updated_at")
    search_fields = ("MedicationName", "Dosage", "VetID__FirstName", "VetID__LastName", "PetID__PetName")
