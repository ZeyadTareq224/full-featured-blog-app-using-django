from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Tag(models.Model):
	name = models.CharField(max_length=50, null=True)
	def __str__(self):
		return self.name


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=100, null=True)
	content = RichTextField(blank=True, null=True)
	#content = models.TextField(null=True)
	img = models.ImageField(null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	comment = models.TextField(max_length=300, null=True)
	created_date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.comment