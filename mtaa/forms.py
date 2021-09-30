from  django import forms
from django.db import models
from django.db.models import fields
from django.forms.forms import Form
from django.forms.models import ModelForm
from .models import NeigbourHood,Post,Business

# code here
class NeighbourhoodForm(forms.ModelForm):
    
    class Meta:
        model = NeigbourHood
        fields = ("hood_name","occupants_count","location")
        
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","body","author")
 
class BizForm(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = ("business_name","business_email","neighbourhood")