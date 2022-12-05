"""sigho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from sitehandler.views import *

urlpatterns = [
    path('dj-admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path('about/',aboutpage,name='aboutpage'),
    path('user/login/',loginpage,name='loginpage'),
    path('admin/login/',Login_admin,name='login_admin'),
    path('admin/home/',AdminHome,name='adminhome'),
    path('admin/logout/',Logout_admin,name='adminlogout'),
    path('admin/create/doctor/',adminaddDoctor,name='adminaddDoctor'),
    path('admin/doctors/list/',adminviewDoctor,name='adminviewDoctor'),
    path('admin/update/doctor/<int:pid>',admin_change_Doctor,name='change_doctor'),
    path('admin/delete/doctor<int:pid><str:email>',admin_delete_doctor,name='admin_delete_doctor'),
    path('admin/create/receptionist/',adminaddReceptionist,name='adminaddReceptionist'),
    path('admin/receptionists/list/',adminviewReceptionist,name='adminviewReceptionist'),
    path('admin/update/receptionist/<int:pid>',admin_change_Receptionist,name='change_receptionist'),
    path('admin/delete/receptionist<int:pid>,<str:email>',admin_delete_receptionist,name='admin_delete_receptionist'),
    path('create/patient',receptionaddpatient,name='receptionaddpatient'),
    path('patients/list',receptionviewPatients,name='receptionviewPatients'),
    path('update/patient/<int:pid>',reception_change_patient,name='change_patient'),
    path('detail/patient/<int:pid>',patientdetail,name='patient_detail'),
    path('delete/patient/<int:pid>',reception_delete_patient,name='delete_patient'),
    path('appointments/list',receptionapointmentlist,name='receptionapointmentlist'),
    path('delete/appoitment<int:pid>',reception_delete_appoitment,name='reception_delete_appoitment'),
    #path('adminviewAppointment/',adminviewAppointment,name='adminviewAppointment'),
    path('home/',Home,name='home'),
    path('profile/',profile,name='profile'),
    path('create/appointment/',MakeAppointments,name='makeappointments'),
    path('appointments/calendar/',viewappointments,name='viewappointments'),
    #path('makeincome/',MakeIncome,name='makeincome'),
    path('logout/',Logout,name='logout'),
    path('footer/',footer,name='footer'),
    path('calculator_imc/',calculator_imc,name='calculator_imc'),
    path('calculator_iw/',calculator_iw,name='calculator_iw'),
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
