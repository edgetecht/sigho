from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def homepage(request):
	return render(request,'index.html')

def aboutpage(request):
	return render(request,'about.html')

def footer(request):
    return render(request,'footer.html')

def calculator_imc(request):
    return render(request,'calculator_imc.html')

def calculator_iw(request):
    return render(request,'calc_ideal_weight.html')

# def Login_admin(request):
#     return render(request,'adminlogin.html')

def Login_admin(request):
	error = ""
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username=u,password=p)
		try:
			if user.is_superuser:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d = {'error' : error}
	print(d)
	return render(request,'admin/adminlogin.html',d)

def loginpage(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				login(request,user)
				error = "no"
				g = request.user.groups.all()[0].name
				if g == 'Doctor':
					page = "doctor"
					d = {'error': error,'page':page}
					return render(request,'doctorhome.html',d)
				elif g == 'Receptionist':
					page = "reception"
					d = {'error': error,'page':page}
					return render(request,'receptionhome.html',d)
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print(e)
			#raise e
	return render(request,'login.html')

def adminaddDoctor(request):
	error = ""
	user="none"
	if not request.user.is_superuser:
		return redirect('login_admin')

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword =  request.POST['repeatpasssword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['dateofbirth']
		bloodgroup = request.POST['bloodgroup']
		specialization = request.POST['specialization']

		try:
			if password == repeatpassword:
				Doctor.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup,specialization=specialization)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				doc_group = Group.objects.get(name='Doctor')
				doc_group.user_set.add(user)
				user.save()
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
	d = {'error' : error}
	return render(request,'admin/adminadddoctor.html',d)

def adminviewDoctor(request):
	if not request.user.is_superuser:
		return redirect('login_admin')
	doc = Doctor.objects.all()
	d = { 'doc' : doc }
	return render(request,'admin/adminviewDoctors.html',d)

def admin_change_Doctor(request,pid):
    error = ""
    if not request.user.is_superuser:
        return redirect('login_admin')
    alldoctors = Doctor.objects.filter(id=pid)
    d = { 'alldoctors' : alldoctors }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        try:
            Doctor.objects.filter(id=pid).update(name=name,email=email,phonenumber=phonenumber,address=address)
            error = "no"
        except:
            error = "yes"
        e = { 'error' : error }
        return render(request,'admin/adminchangedoctor.html',e)
    elif request.method == 'GET':
        return render(request,'admin/adminchangedoctor.html', d)

def admin_delete_doctor(request,pid,email):
	if not request.user.is_superuser:
		return redirect('login_admin')
	doctor = Doctor.objects.get(id=pid)
	doctor.delete()
	users = User.objects.filter(username=email)
	users.delete()
	return redirect('admin/adminviewDoctor')



def adminaddReceptionist(request):
	error = ""
	if not request.user.is_superuser:
		return redirect('login_admin')

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['dateofbirth']
		bloodgroup = request.POST['bloodgroup']

		try:
			if password == repeatpassword:
				Receptionist.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				rec_group = Group.objects.get(name='Receptionist')
				rec_group.user_set.add(user)
				#print(rec_group)
				user.save()
				#print(user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d = { 'error' : error }
	return render(request,'admin/adminaddreceptionist.html',d)

def admin_change_Receptionist(request,pid):
    error = ""
    if not request.user.is_superuser:
        return redirect('login_admin')
    allreceptionist = Receptionist.objects.filter(id=pid)
    r = { 'allreceptionist' : allreceptionist }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        address = request.POST['address']
        try:
            Receptionist.objects.filter(id=pid).update(name=name,email=email,phonenumber=phonenumber,address=address)
            error = "no"
        except:
            error = "yes"
        e = { 'error' : error }
        return render(request,'admin/adminchangereceptionist.html',e)
    elif request.method == 'GET':
        return render(request,'admin/adminchangereceptionist.html', r)

def adminviewReceptionist(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	rec = Receptionist.objects.all()
	r = { 'rec' : rec }
	return render(request,'admin/adminviewreceptionists.html',r)

def admin_delete_receptionist(request,pid,email):
	if not request.user.is_staff:
		return redirect('login_admin')
	reception = Receptionist.objects.get(id=pid)
	reception.delete()
	users = User.objects.filter(username=email)
	users.delete()
	return redirect('admin/adminviewReceptionist')

def adminviewAppointment(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	upcomming_appointments = Appointment.objects.filter(appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
	#print("Upcomming Appointment",upcomming_appointments)
	previous_appointments = Appointment.objects.filter(appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(status=False).order_by('-appointmentdate')
	#print("Previous Appointment",previous_appointments)
	d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
	return render(request,'admin/adminviewappointments.html',d)


def Logout(request):
	if not request.user.is_active:
		return redirect('loginpage')
	logout(request)
	return redirect('loginpage')

def Logout_admin(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	logout(request)
	return redirect('login_admin')

def AdminHome(request):
	#after login user comes to this page.
	if not request.user.is_staff:
		return redirect('login_admin')
	return render(request,'admin/adminhome.html')

def Home(request):
	if not request.user.is_active:
		return redirect('loginpage')
	g = request.user.groups.all()[0].name
	if g == 'Doctor':
		return render(request,'doctorhome.html')
	elif g == 'Receptionist':
		return render(request,'receptionhome.html')

def profile(request):
	if not request.user.is_active:
		return redirect('loginpage')
	g = request.user.groups.all()[0].name
	if g == 'Doctor':
		doctor_detials = Doctor.objects.all().filter(email=request.user)
		d = { 'doctor_detials' : doctor_detials }
		return render(request,'doctorprofile.html',d)
	elif g == 'Receptionist':
		reception_details = Receptionist.objects.all().filter(email=request.user)
		d = { 'reception_details' : reception_details }
		return render(request,'receptionprofile.html',d)

def patientdetail(request,pid):
	if not request.user.is_active:
		return redirect('loginpage')
	patient = Patient.objects.get(id=pid)
	p = { 'patient' : patient}
	return redirect('receptionpatdetail')

def receptionaddpatient(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	g = request.user.groups.all()[0].name
	if g == 'Receptionist':
		if request.method == 'POST':
			first_name = request.POST['first_name']
			last_name =request.POST['last_name']
			ci = request.POST['ci']
			phonenumber = request.POST['phonenumber']
			address = request.POST['address']
			bloodgroup = request.POST['bloodgroup']
			weight = request.POST['weight']
			height = request.POST['height']
			result_imc = request.POST['result_imc']
			# try:
			# 	imc = request.POST.get['imc', False]
			# except MultiValueDictKeyError:
			# 	imc = False
			try:
				Patient.objects.create(first_name=first_name,last_name=last_name,ci=ci,phonenumber=phonenumber,address=address,bloodgroup=bloodgroup,weight=weight,height=height,result_imc=result_imc)
				error = "no"
			except:
				error = "yes"
	e = {"error":error}
	return render(request,'receptionaddpatient.html',e)
	#return render(request,'createaccount.html')

def reception_delete_patient(request,pid):
	if not request.user.is_active:
		return redirect('loginpage')
	patient = Patient.objects.get(id=pid)
	patient.delete()
	return redirect('receptionviewPatients')


def reception_change_patient(request,pid):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	allpatients = Patient.objects.filter(id=pid)
	p = { 'allpatients' : allpatients}
	#patient = Patients.objects.all(id=pid)
	if request.method == 'POST':
			first_name = request.POST['first_name']
			last_name =request.POST['last_name']
			ci = request.POST['ci']
			phonenumber = request.POST['phonenumber']
			address = request.POST['address']
			bloodgroup = request.POST['bloodgroup']
			weight = request.POST['weight']
			height = request.POST['height']
			result_imc = request.POST['result_imc']
			try:
				Patient.objects.filter(id=pid).update(first_name=first_name,last_name=last_name,ci=ci,phonenumber=phonenumber,address=address,bloodgroup=bloodgroup,weight=weight,height=height,result_imc=result_imc)
				error = "no"
			except:
				error = "yes"
			e = { "error" : error }
			return render(request,'receptionchangepatient.html', e)
	elif request.method == 'GET':
			#print(d)
			return render(request,'receptionchangepatient.html', p)


def receptionviewPatients(request):
	if not request.user.is_active:
		return redirect('loginpage')
	pat = Patient.objects.all()
	d = { 'pat' : pat }
	return render(request,'receptionviewPatients.html',d)

def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	alldoctors = Doctor.objects.all()
	allpatients = Patient.objects.all()
	d = { 'alldoctors' : alldoctors, 'allpatients' : allpatients }
	g = request.user.groups.all()[0].name
	if g == 'Receptionist':
		if request.method == 'POST':
			doctoremail = request.POST['doctoremail']
			doctorname = request.POST['doctorname']
			patientname = request.POST['patientname']
			appointmentdate = request.POST['appointmentdate']
			appointmenttime = request.POST['appointmenttime']
			symptoms = request.POST['symptoms']
			try:
				Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,patientname=patientname,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescription="")
				error = "no"
			except:
				error = "yes"
			e = {"error":error}
			return render(request,'receptionmakeappointments.html',e)
		elif request.method == 'GET':
			#print(d)
			return render(request,'receptionmakeappointments.html', d)#

def reception_delete_appoitment(request,pid):
	if not request.user.is_active:
		return redirect('loginpage')
	appointment = Appointment.objects.get(id=pid)
	appointment.delete()
	return redirect('receptionapointmentlist')

def receptionapointmentlist(request):
	if not request.user.is_active:
		return redirect('loginpage')
	appo = Appointment.objects.filter(appointmentdate__gte=timezone.now(),status=True).order_by('appointmentdate')
	a = { 'appo' : appo }
	return render(request,'receptionapointmentlist.html', a)

def viewappointments(request):
	if not request.user.is_active:
		return redirect('loginpage')
	#print(request.user)
	g = request.user.groups.all()[0].name
	if g == 'Doctor':
		if request.method == 'POST':
			prescriptiondata = request.POST['prescription']
			idvalue = request.POST['idofappointment']
			Appointment.objects.filter(id=idvalue).update(prescription=prescriptiondata,status=False)
			#print(idvalue)
			#print(pname)
			#p = {"idvalue":idvalue,"pname":pname}
			#return render(request,'doctoraddprescription.html',p)
		upcomming_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__gte=timezone.now(),status=True).order_by('-appointmentdate')
		#print("Upcomming Appointment",upcomming_appointments)
		previous_appointments = Appointment.objects.filter(doctoremail=request.user,appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail=request.user,status=False).order_by('-appointmentdate')
		#print("Previous Appointment",previous_appointments)
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'doctorviewappointment.html',d)
	elif g == 'Receptionist':
		upcomming_appointments = Appointment.objects.filter(appointmentdate__gte=timezone.now(),status=True).order_by('-appointmentdate')
		#print("Upcomming Appointment",upcomming_appointments)
		previous_appointments = Appointment.objects.filter(appointmentdate__lt=timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(status=False).order_by('-appointmentdate')
		#print("Previous Appointment",previous_appointments)
		d = { "upcomming_appointments" : upcomming_appointments, "previous_appointments" : previous_appointments }
		return render(request,'receptionviewappointments.html',d)

def receptionaddtest(request):
    error = ""
    if not request.user.is_active:
        return redirect('loginpage')
    allpatients = Patient.objects.all()
    p = { 'allpatients' : allpatients}
    g = request.user.groups.all()[0].name
    if g == 'Receptionist':
        if request.method == 'POST':
            tipo = request.POST['tipo']
            paciente = request.POST['paciente']
            resultado = request.POST['resultado']
            tratramiento = request.POST['tratramiento']
            try:
                Examen.objects.create(tipo=tipo,paciente=paciente,resultado=resultado,tratramiento=tratramiento)
                error = "no"
            except:
                error = "yes"
            e = { "error" : error }
            return render(request,'receptionaddtest.html', e)
        elif request.method == 'GET':
            return render(request,'receptionaddtest.html', p)


# def MakeIncome(request):
#     error = ""
#     if not request.user.is_active:
#         return redirect('loginpage')
#     alldoctors = Doctor.objects.all()
#     d = { 'alldoctors' : alldoctors }
#     g = request.user.groups.all()[0].name
#     if g == 'Receptionist':
#         if request.method == 'POST':
#             doctoremail = request.POST['doctoremail']
#             doctorname = request.POST['doctorname']
#             patientname = request.POST['patientname']
#             gestationtime = request.POST['gestationtime']
#             incometime = request.POST['incometime']
#             incomedate = request.POST['incomedate']
#             bad = request.POST['bad']
#             try:
#                 Income.objects.create(doctorname=doctorname,doctoremail=doctoremail,patientname=patientname,gestationtime=gestationtime,incometime=incometime,incomedate=incomedate,bad=bad)
#                 error = "no"
#             except:
#                 error = "yes"
#                 e = {"error":error}
#                 return render(request,'receptionmakeincome.html',e)
#     elif request.method == 'GET':
#         return render(request,'receptionmakeincome.html',d)
