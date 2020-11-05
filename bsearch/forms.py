from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper
import cloudinary
       
class RegisterForm(RegistrationForm):
    username = forms.CharField(max_length=255)
        
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True 


class NewDonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        exclude = ['Admin', 'pub_date', 'admin_profile']
        widgets = {
          'address': forms.Textarea(attrs={'rows':1, 'cols':5,}),
        }


class NewCountyForm(forms.ModelForm):
    class Meta:
        model = County
        exclude = ['Admin', 'pub_date', 'admin_profile']

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':1, 'cols':5,}),
        }
        
