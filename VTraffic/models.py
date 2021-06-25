from django.db import models


VIOLATION_CHOICE = (('No Drivers License', 'no drivers license'),('Expired Drivers License', 'expired drivers license'),('Drunk Driving', 'drunk driving'),('Reckless Driving', 'reckless driving'),('No MC Helmet', 'no mc helmet'),('OR/CR Or Drivers License Not Carried', 'or/cr or drivers license not carried'),('Fake OR/CR And Sticker', 'fake or/or plates and sticker'),('Driving With Defective Parts And Accessories', 'driving with defective parts and accessories'),('No Sign Board', 'no sign board'),('Unregistered Motor Vehicle', 'unregistered motor vehicle'),('Improvised/Unauthorized Mutter', 'improvised/unauthorized mutter'),('No Signal Lights', 'no signal lights'),('No Tail Lights', 'no tail lights'),('No Head Lights', 'no head lights'),('No Side Mirrors', 'no side mirrors'),('No Horns', 'no horns'),('Defective Brake', 'defective brake'),('Illegal Parking', 'illegal parking'),('Dirty/No/Not Firmly Attached Plate Number', 'dirty/no/not firmly attached plate number'),('Obstruction', 'obstruction'))


class main(models.Model):
	identification = models.CharField(default="", max_length=200)
	def Identification_Get(self):
		return self.Identification

class Officer(models.Model):

	Officer = models.CharField(max_length=200)
	Violator = models.CharField(max_length=200)
	LicenseNo = models.CharField(max_length=200, blank=True)
	Date = models.DateField(blank=True, null=True)
	Violation = models.IntegerField(max_length=200, choices=VIOLATION_CHOICE)
	Fine = models.CharField(max_length=200)
	Email = models.CharField(max_length=200)

class violator(models.Model):
	Ticket = models.ForeignKey(Officer, default=None, null=True, on_delete=models.CASCADE)

class communicate(models.Model):
	FirstName = models.CharField(max_length=200)
	LastName = models.CharField(max_length=200)
	EmailAddress = models.CharField(max_length=200)
	GiveUsFeedback = models.CharField(max_length=200)

class checkout(models.Model):
	Violation = models.ForeignKey(Officer, on_delete=models.CASCADE, null=True)
	FineAmount = models.FloatField()
	






