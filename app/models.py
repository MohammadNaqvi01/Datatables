from django.db import models

# Create your models here.

class UserModel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    designation=models.CharField(max_length=50)




from django.forms import ModelForm
from django import forms
from .models import UserModel
from django.utils.translation import gettext_lazy as _



class UserModelForm(ModelForm):

    class Meta:
        model = UserModel

        fields='__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                      'class':'form-control',
                      
                        }),
            'email':forms.EmailInput(attrs={
                         'class':'form-control',
                         
                          }),
            'designation':forms.TextInput(attrs={
                         'class':'form-control',
                        
                           }) 
        }

        labels={
            'name':'Name',
            'email':'Email',
            'designation':'Role'
        }