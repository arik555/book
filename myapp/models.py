from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200, null=False, blank=False)

	def __str__(self):
		return self.name


class Ebook(models.Model):
	RAW_CHOICES = [
		('1', 'GitHub'),
		('2', 'Google'),
		('3', 'Direct'),
	]
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='my_ebooks')
	title = models.CharField(max_length=200, null=False, blank=False)
	author = models.CharField(max_length=500, help_text='Add multiple authors with semicolon at the end of each.', null=False, blank=False)
	link = models.CharField(max_length=1000, null=False, blank=False)
	source = models.CharField(choices=RAW_CHOICES, max_length=1)

	class Meta:
		ordering = ['-id']


	def __str__(self):
		return self.title

	def list_authors(self):
		return self.author.split(";")

	def frame_src(self):
		if self.source == '2':
			return "https://docs.google.com/viewer?url="+self.link+"&hl=en&embedded=true"
		# elif self.source == '1':
			# import requests
			# print(self.link)
			# r = requests.post("https://nbviewer.jupyter.org/create/", data={'gistnorurl': self.link})
			# return r.url+"#view=FitH"
		else:
			return self.link+"#view=FitH"

