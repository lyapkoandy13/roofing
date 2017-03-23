from django import forms
from main.models import Good

class GoodForm(forms.ModelForm):
	class Meta:
		model = Good
		fields = ('name', 'description', 'price', 'images')