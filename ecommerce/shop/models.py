from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class Category(models.Model):
     name = models.CharField(max_length=200)
     date_added = models.DateTimeField(auto_now=True)
     class Meta:
        ordering = ['-date_added']
     def __str__(self):
       return self.name
            
class Prodect (models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=5000)
    category = models.ForeignKey (Category, related_name='categorie', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=5000)

    class Meta:
        ordering = ['-date_add']
    def __str__(self):
       return self.title
class UserRegister(UserCreationForm):
    email= forms.EmailField()
    tel= forms.IntegerField(validators=[MaxValueValidator(99999999)])
    adress=forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','tel','adress','password1','password2']
    

