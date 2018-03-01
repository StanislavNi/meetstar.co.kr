from django import forms
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'username' , 'first_name', 'last_name', 'email',
                  'bio', 'location', 'birth_date', 'password',
                  ]
        widgets = {
            'birth_date': forms.DateTimeInput(
                attrs={'class': 'datetime-input'})
        }
