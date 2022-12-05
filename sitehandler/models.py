from django.db import models

class Doctor(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)
	specialization = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Receptionist(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Patient(models.Model):
	id = models.AutoField(primary_key = True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	ci = models.CharField(max_length=11)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	bloodgroup = models.CharField(max_length=5)
	weight = models.CharField(max_length=10)
	height = models.CharField(max_length=10)
	result_imc = models.CharField(max_length=10)
 
	def __str__(self):
		return self.first_name

class Appointment(models.Model):
    id = models.AutoField(primary_key = True)
    doctorname = models.CharField(max_length=50)
    doctoremail = models.EmailField(max_length=50)
    patientname = models.CharField(max_length=50)
    appointmentdate = models.DateField(max_length=10)
    appointmenttime = models.TimeField(max_length=10)
    symptoms = models.CharField(max_length=100)
    status = models.BooleanField()
    prescription = models.CharField(max_length=200)

    def __str__(self):
        return self.patientname + " usted tiene una cita con " + self.doctorname

class Examen(models.Model):
    id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length=20)
    paciente = models.ForeignKey(Patient, on_delete=models.CASCADE)
    #doctor_asigna = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=200)
    tratramiento = models.CharField(max_length=200)
    id = models.AutoField(primary_key = True)
    
    def __str__(self):
    		return self.tipo

# class Income(models.Model):
# 	doctorname = models.CharField(max_length=50)
# 	doctoremail = models.EmailField(max_length=50)
# 	patientname = models.CharField(max_length=50)
# 	#ci = models.IntegerField()
# 	address = models.CharField(max_length=100)
# 	symptoms = models.CharField(max_length=200)
# 	status = models.BooleanField()
# 	prescription = models.CharField(max_length=200)
# 	incomedate = models.DateField(max_length=10)
# 	incometime = models.TimeField(max_length=10)
# 	gestationtime = models.CharField(max_length=200)
# 	bed = models.CharField(max_length=3)

# 	def __str__(self):
# 		return self.patientname
