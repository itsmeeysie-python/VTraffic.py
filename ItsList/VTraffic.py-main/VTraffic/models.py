from django.db import models


VIOLATION_CHOICE = (('No Drivers License', 'no drivers license'),('Expired Drivers License', 'expired drivers license'),('Drunk Driving', 'drunk driving'),('Reckless Driving', 'reckless driving'),('No MC Helmet', 'no mc helmet'),('OR/CR Or Drivers License Not Carried', 'or/cr or drivers license not carried'),('Fake OR/CR And Sticker', 'fake or/or plates and sticker'),('Driving With Defective Parts And Accessories', 'driving with defective parts and accessories'),('No Sign Board', 'no sign board'),('Unregistered Motor Vehicle', 'unregistered motor vehicle'),('Improvised/Unauthorized Mutter', 'improvised/unauthorized mutter'),('No Signal Lights', 'no signal lights'),('No Tail Lights', 'no tail lights'),('No Head Lights', 'no head lights'),('No Side Mirrors', 'no side mirrors'),('No Horns', 'no horns'),('Defective Brake', 'defective brake'),('Illegal Parking', 'illegal parking'),('Dirty/No/Not Firmly Attached Plate Number', 'dirty/no/not firmly attached plate number'),('Obstruction', 'obstruction'))

STATUS_CHOICE = (('Pending', 'pending'),('Penalty', 'penalty'),('Settled', 'settled'))

class First_Page(models.Model):
	identification = models.CharField(default="", max_length=200)
	def Identification_Get(self):
		return self.Identification

class Officer_Page(models.Model):

	Officer = models.CharField(max_length=200)
	Violator = models.CharField(max_length=200)
	LicenseNo = models.CharField(max_length=200, blank=True)
	Date = models.DateField(blank=True, null=True)
	Violation = models.IntegerField(max_length=200, choices=VIOLATION_CHOICE)
	Fine = models.CharField(max_length=200)
	Email = models.CharField(max_length=200)

class Ticket(models.Model):
	Ticket = models.ForeignKey(Officer_Page, default=None, null=True, on_delete=models.CASCADE)
	DueDate = models.DateField()
	Status = models.CharField(max_length=200, choices=STATUS_CHOICE, default='pending')

class Notification(models.Model):
	Reminders = models.TextField()
	Date = models.DateField(auto_now=True)
	Status = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)

class Payment(models.Model):
	Violation = models.ForeignKey(Officer_Page, on_delete=models.CASCADE, null=True)
	FineAmount = models.FloatField()
	Status = models.CharField(max_length=200, choices=STATUS_CHOICE, default=None)






