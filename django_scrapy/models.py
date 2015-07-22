
# Create your models here.
from django.db import models
	
class questions_urls(models.Model):
	question = models.CharField()
	url = models.CharField()