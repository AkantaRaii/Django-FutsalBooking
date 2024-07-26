from django import forms
from .models import booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# class userform(forms.Form):
#     fname=forms.CharField(max_length=50)
#     lname=forms.CharField(max_length=50,required=False)
#     phone=forms.CharField(max_length=10)
class signupform(UserCreationForm):
    
    user_phone = forms.CharField(required=True, max_length=10)

    class Meta:
        model = User
        fields = ['username', 'user_phone', 'password1', 'password2']
class futsalforms(forms.Form):
    futsal_name=forms.CharField(max_length=50)
    futsal_court_phone=forms.CharField(max_length=10)
    futsal_court_address=forms.CharField(max_length=50)
    price_per_hour = forms.DecimalField(max_digits=6, decimal_places=2)

class searchform(forms.Form):
    query=forms.CharField(label='search')

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['user', 'start_time','duration']