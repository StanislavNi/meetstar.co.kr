from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

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

class UserCreateForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user
