from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import ContactUs,Volunteer,Registration,Volunteer,CellName,EventName
from django.shortcuts import redirect
from django.core.exceptions import ValidationError




class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'username','type':'text','placeholder':'username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'email','type':'email','placeholder':'your email'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'password1','type':'password','placeholder':'password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'password2','type':'password','placeholder':'Re-type password'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class ContactForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'first','type':'text','placeholder':'First name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'last','type':'text','placeholder':'last name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'email','type':'email','placeholder':'Your email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'phone','type':'text','placeholder':'10-digits number'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'message','type':'text','placeholder':'Your message'}))

    class Meta:
        model = ContactUs
        fields = '__all__'




class ProfileForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'name','type':'text','placeholder':'Your name'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'phone','type':'text','placeholder':'10-digits number'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'email','type':'email','placeholder':'Your email'}))
    college = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'college','type':'text','placeholder':'Your college'}))
    profile_pic = forms.ImageField()

    class Meta:
        model = Volunteer
        fields = '__all__'
        exclude = ['user','name_admin','qr_code']

    
    
# class RegistrationForm(ModelForm):
#     volunteer =forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput())
#     cell = forms.ModelChoiceField(queryset=CellName.objects.all(),widget=forms.HiddenInput())
#     event_name = forms.ModelChoiceField(queryset=EventName.objects.all(),widget=forms.HiddenInput())
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'name','type':'text','placeholder':'Your name'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'email','type':'email','placeholder':'Your email'}))
#     college = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'college','type':'text','placeholder':'Your college'}))
#     college_rn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'college_rn','type':'text','placeholder':'Your college roll number'}))
#     city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'city','type':'text','placeholder':'Your college city'}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','id': 'phone','type':'text','placeholder':'10-digits number'}))
#     team = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-box','value':'','id': 'team','type':'text','placeholder':'Your team name','onkeydown':'upperCaseF(this)'}))
    
#     class Meta:
#         model = Registration
#         fields = '__all__'
#         exclude = ['team']
     




    
