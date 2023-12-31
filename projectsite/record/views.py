# myapp/views.py
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from record.models import Vet, Pet, Appointment, Treatment, Prescription
from record.forms import VetForm, PetForm, AppointmentForm, TreatmentForm, PrescriptionForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Pet
    context_object_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VetListView(ListView):
    model = Vet
    template_name = 'vet-list.html'
    context_object_name = 'vets'
    paginate_by = 5

    def get_queryset(self):
        return Vet.objects.all()

class VetCreateView(CreateView):
    model = Vet
    form_class = VetForm
    template_name = 'vet-add.html'
    success_url = reverse_lazy('vet-list')

class VetUpdateView(UpdateView):
    model = Vet
    form_class = VetForm
    template_name = 'vet-edit.html'
    success_url = reverse_lazy('vet-list')

class VetDeleteView(DeleteView):
    model = Vet
    template_name = 'vet-del.html'
    success_url = reverse_lazy('vet-list')

class PetListView(ListView):
    model = Pet
    template_name = 'pet-list.html'
    context_object_name = 'pets'
    paginate_by = 5

    def get_queryset(self):
        return Pet.objects.all()

class PetCreateView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet-add.html'
    success_url = reverse_lazy('pet-list')

class PetUpdateView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pet-edit.html'
    success_url = reverse_lazy('pet-list')

class PetDeleteView(DeleteView):
    model = Pet
    template_name = 'pet-del.html'
    success_url = reverse_lazy('pet-list')

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointment-list.html'
    context_object_name = 'appointments'
    paginate_by = 5

    def get_queryset(self):
        return Appointment.objects.all()

class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment-add.html'
    success_url = reverse_lazy('appointment-list')

class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment-edit.html'
    success_url = reverse_lazy('appointment-list')

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment-del.html'
    success_url = reverse_lazy('appointment-list')

class TreatmentListView(ListView):
    model = Treatment
    template_name = 'treatment-list.html'
    context_object_name = 'treatments'
    paginate_by = 5

    def get_queryset(self):
        return Treatment.objects.all()

class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment-add.html'
    success_url = reverse_lazy('treatment-list')

class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = 'treatment-edit.html'
    success_url = reverse_lazy('treatment-list')

class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = 'treatment-del.html'
    success_url = reverse_lazy('treatment-list')

class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'prescription-list.html'
    context_object_name = 'prescriptions'
    paginate_by = 5

    def get_queryset(self):
        return Prescription.objects.all()

class PrescriptionCreateView(CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'prescription-add.html'
    success_url = reverse_lazy('prescription-list')

class PrescriptionUpdateView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'prescription-edit.html'
    success_url = reverse_lazy('prescription-list')

class PrescriptionDeleteView(DeleteView):
    model = Prescription
    template_name = 'prescription-del.html'
    success_url = reverse_lazy('prescription-list')
