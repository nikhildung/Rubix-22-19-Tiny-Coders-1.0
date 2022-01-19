from django.db import models

# Create your models here.
class Doctor(models.Model):
    D_id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    D_name = models.CharField(max_length=100)
    D_email = models.CharField(max_length=100)
    D_age = models.DecimalField(max_digits=3, decimal_places=0)
    D_number = models.DecimalField(max_digits=3, decimal_places=0)


    def __str__(self):
        return f"{self.D_id}, {self.D_name}, {self.D_email}, {self.D_email}, {self.D_age}, {self.D_number} "

class Patient(models.Model):
    P_id = models.DecimalField(max_digits=4, decimal_places=0,primary_key=True)
    P_name = models.CharField(max_length=100)
    P_email = models.CharField(max_length=100)
    P_age = models.DecimalField(max_digits=3,decimal_places=0)
    P_number = models.DecimalField(max_digits=3,decimal_places=0)
    P_medicalrecord = models.CharField(max_length=200)
    D_id = models.ForeignKey(Doctor,on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.P_id}, {self.P_name}, {self.P_email}, {self.P_age}, {self.P_number}, {self.P_medicalrecord} "

class prescription(models.Model):
    Pr_id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    Pr_detail = models.CharField(max_length=100)
    Pr_medicalrecord = models.CharField(max_length=100)
    P_id = models.ForeignKey(Patient,on_delete=models.CASCADE)
    D_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Pr_id}, {self.Pr_details}, {self.Pr_medicalrecord}"

class Bill(models.Model):
    B_id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    B_total = models.DecimalField(max_digits=6, decimal_places=0)
    P_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.B_id}, {self.B_total}"

class appointment(models.Model):
    app_id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    app_purpose = models.CharField(max_length=500)
    app_request = models.CharField(max_length=100,default="")
    app_link = models.CharField(max_length=100,default="")
    P_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    D_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.app_id}, {self.app_purpose}"

class Medicine(models.Model):
    m_id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    m_name = models.CharField(max_length=100)
    m_price = models.DecimalField(max_digits=4, decimal_places=0)
    P_id = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.m_id}, {self.m_name}, {self.m_price}"



