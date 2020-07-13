from django.forms import ModelForm
from django import forms
from .models import Post, Comment


class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'img', 'tag']


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['comment']