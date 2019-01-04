from django.db import models
from django.conf import settings
# Create your models here.



class event(models.Model):
	#owner = models.ForeignKey(User,null=False)
	event_name = models.CharField(max_length=100)
	event_location = models.CharField(max_length=30)
	event_date = models.DateField(auto_now=False , null=False)
	event_posting_date = models.DateField(auto_now=True)

	def __str__(self):
		return self.event_name