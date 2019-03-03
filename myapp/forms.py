from django import forms
from .models import Category, Ebook

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'


class EbookForm(forms.ModelForm):
	class Meta:
		model = Ebook
		fields = '__all__'
