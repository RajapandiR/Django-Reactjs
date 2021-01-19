from django import forms
from djangoapp import models

# Create your models here.
class StudForm(forms.ModelForm):
	class Meta:
		fields = '__all__'
		model = models.StudModel 