from django import forms
from .models import User
 
class Add_A_User(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'gender', 'phone_number']
