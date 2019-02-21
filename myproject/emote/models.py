from django.db import models

intensityChoices = (
	('1', '1 (Drained / Exhausted)'),
	('2', '2 (Foggy)'),
	('3', '3 (OK / Normal)'),
	('4', '4 (Agitated)'),
	('5', '5 (Screaming Inside)')
)

incidentTypeChoices = (
	('Panic Attack', 'Panic Attack'),
	('Extreme Depression', 'Extreme Depression'),
)

class Checkin(models.Model):
	person = models.CharField(max_length=300, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	feeling = models.CharField(max_length=300)
	intensity = models.CharField(max_length=300, choices=intensityChoices)
	location = models.CharField(max_length=300)
	details = models.TextField()
	
	
class Incident(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	incidentType = models.CharField(max_length=300, choices=incidentTypeChoices)
	location = models.CharField(max_length=300)
	details = models.TextField()
	
	
class Quote(models.Model):
	quote = models.TextField()
