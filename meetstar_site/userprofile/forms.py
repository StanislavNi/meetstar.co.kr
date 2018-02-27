from django import forms
from .models import Profile,User

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'id', 'username' , 'first_name', 'last_name',
                  'bio', 'location', 'birth_date',
                  'email', 'password'
                  ]
