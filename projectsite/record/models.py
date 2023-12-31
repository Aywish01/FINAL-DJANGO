from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Vet(BaseModel):
    VetID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField()
    ClinicName = models.CharField(max_length=255)
    ProfileImage = models.ImageField(upload_to='vet_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.ProfileImage} {self.FirstName} {self.LastName}"

class Pet(BaseModel):
    PetID = models.IntegerField(primary_key=True)
    PetName = models.CharField(max_length=255)
    Species = models.CharField(max_length=255)
    Breed = models.CharField(max_length=255)
    BirthDate = models.DateField()
    Owner = models.CharField(max_length=255) # Change this to IntegerField

    def __str__(self):
        return self.PetName

class Appointment(BaseModel):
    PetID = models.ForeignKey(Pet, on_delete=models.CASCADE)
    AppointmentDate = models.DateTimeField()
    Purpose = models.TextField()

class Treatment(BaseModel):
    TreatmentID = models.AutoField(primary_key=True)
    TreatmentName = models.CharField(max_length=255)
    Description = models.TextField()
    PetID = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.TreatmentName



class Prescription(BaseModel):
    PrescriptionID = models.AutoField(primary_key=True)
    MedicationName = models.CharField(max_length=255)
    Dosage = models.CharField(max_length=255)
    VetID = models.CharField(max_length=50, null=True, blank=True)
    PetID = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Prescription for {self.PetID}: {self.MedicationName} - {self.Dosage}"
