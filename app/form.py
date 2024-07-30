from django import forms
from .models import booking,futsal_court
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class signupform(UserCreationForm):
    
    user_phone = forms.CharField(required=True, max_length=10)

    class Meta:
        model = User
        fields = ['username', 'user_phone', 'password1', 'password2']
# it is a forms.ModelForm which binds form to model automatically 
class futsalforms(forms.ModelForm):
    futsal_name=forms.CharField(max_length=10)
    futsal_court_phone=forms.CharField(max_length=10)
    futsal_court_address=forms.CharField(max_length=50)
    price_per_hour = forms.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        model=futsal_court
        fields=['futsal_court_phone','futsal_name','futsal_court_address','price_per_hour']

# it is a forms.Forms that we have to maually bind to model
class searchform(forms.Form):
    query=forms.CharField(label='search')


class BookingForm(forms.Form):
    start_time = forms.DateTimeField()
    duration = forms.IntegerField()