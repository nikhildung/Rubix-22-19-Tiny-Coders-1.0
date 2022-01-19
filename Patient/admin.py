from django.contrib import admin

from .models import Doctor, Patient, appointment, Medicine, Bill, prescription


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('D_id', 'D_name', 'D_email', 'D_age', 'D_number')


admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('P_id', 'P_name', 'P_email', 'P_age', 'P_number', 'P_medicalrecord')


admin.site.register(Patient, PatientAdmin)


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('Pr_id', 'Pr_detail', 'Pr_medicalrecord')


admin.site.register(prescription, PrescriptionAdmin)


class BillAdmin(admin.ModelAdmin):
    list_display = ('B_id', 'B_total')


admin.site.register(Bill, BillAdmin)


class appointmentAdmin(admin.ModelAdmin):
    list_display = ('app_id', 'app_purpose')


admin.site.register(appointment, appointmentAdmin)


class medicineAdmin(admin.ModelAdmin):
    list_display = ('m_id', 'm_name', 'm_price')


admin.site.register(Medicine, medicineAdmin)
