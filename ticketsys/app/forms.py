# register and login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from . models import Tickets

class registeration(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput(),required=True)
    password=forms.CharField(widget=PasswordInput(),required=True)

class CreateRecordForm(forms.ModelForm):
     class Meta:
        model=Tickets
        fields = ['Name','Cisco_id','Ticket_description','OS_type','Tool','Ticket_State']
class UpdateRecordForm(forms.ModelForm):
     class Meta:
        model=Tickets
        fields = ['Name','Cisco_id','Ticket_description','OS_type','Tool','Ticket_State']

