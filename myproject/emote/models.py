from django.db import models

		<option value="">----------------</option>
		<option value="1">1 (Drained / Exhausted)</option>
		<option value="2">2 (Foggy)</option>
		<option value="3">3 (OK / Normal)</option>
		<option value="4">4 (Agitated)</option>
		<option value="5">5 (Screaming Inside)</option>
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
	
	
