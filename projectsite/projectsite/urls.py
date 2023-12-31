from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from record.views import (
    HomePageView, VetListView, VetCreateView, VetDeleteView, VetUpdateView,
    PetListView, PetCreateView, PetDeleteView, PetUpdateView,
    AppointmentListView, AppointmentCreateView, AppointmentDeleteView, AppointmentUpdateView,
    TreatmentListView, TreatmentCreateView, TreatmentDeleteView, TreatmentUpdateView,
    PrescriptionListView, PrescriptionCreateView, PrescriptionDeleteView, PrescriptionUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('vets/', VetListView.as_view(), name='vet-list'),
    path('vets/add/', VetCreateView.as_view(), name='vet-add'),
    path('vets/<int:pk>/', VetUpdateView.as_view(), name='vet-update'),
    path('vets/<int:pk>/delete/', VetDeleteView.as_view(), name='vet-delete'),
    path('pets/', PetListView.as_view(), name='pet-list'),
    path('pets/add/', PetCreateView.as_view(), name='pet-add'),
    path('pets/<int:pk>/', PetUpdateView.as_view(), name='pet-update'),
    path('pets/<int:pk>/delete/', PetDeleteView.as_view(), name='pet-delete'),
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/add/', AppointmentCreateView.as_view(), name='appointment-add'),
    path('appointments/<int:pk>/update/', AppointmentUpdateView.as_view(), name='appointment-update'),
    path('appointments/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('treatments/', TreatmentListView.as_view(), name='treatment-list'),
    path('treatments/add/', TreatmentCreateView.as_view(), name='treatment-add'),
    path('treatments/<int:pk>/update/', TreatmentUpdateView.as_view(), name='treatment-update'),    
    path('treatments/<int:pk>/delete/', TreatmentDeleteView.as_view(), name='treatment-delete'),
    path('prescriptions/', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescriptions/add/', PrescriptionCreateView.as_view(), name='prescription-add'),
    path('prescriptions/<int:pk>/', PrescriptionUpdateView.as_view(), name='prescription-update'),
    path('prescriptions/<int:pk>/delete/', PrescriptionDeleteView.as_view(), name='prescription-delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
