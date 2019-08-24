from django.db import models
from django.urls import reverse 

class Page(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField()
	last_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('page-detail',kwargs={'page_id':self.id})
