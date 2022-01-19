from . import views
from django.urls import path

urlpatterns =[
    path('',views.Home,name = "Home"),
    path('Doctor',views.Doctor , name="Doctor"),
    path('Doctor_Precription', views.Doctor_Pre, name="Doc_Pre"),
    path('Doctor_Profile', views.Doctor_Profile, name="Doc_Pro"),
    path('Doctor_App', views.Doctor_Appointment, name="Doc_App"),
    path('Signup', views.signup,name="Sign_up"),
    path('Login',views.LOGIN,name="Login"),
    path('Emergency',views.Emergency,name="Emergency"),
    path('Patient_Appointment',views.Patient_Appointmentm, name="App")


]
