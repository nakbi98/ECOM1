from django.core.validators import MaxValueValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    email= forms.EmailField()
    tel= forms.IntegerField(validators=[MaxValueValidator(99999999)])
    adress=forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','tel','adress','password1','password2']
   