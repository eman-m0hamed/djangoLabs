from django import forms
from .models import myUser
class userFom(forms.ModelForm):
    # build form
    class Meta:
        model = myUser
        fields = {'name', 'email', 'password'}
        labels = {
            'name' : 'Name',
            'email' : 'Email',
            'password' : 'Password'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': "Enter Your Name"}),
            'email' : forms.EmailInput(attrs={'placeholder': "Enter Your Email"}),
            'password' : forms.TextInput(attrs={'placeholder': "Enter Your Password"}),
        }

        help_texts = {
            'name' : "Please Enter a valid name<br><br>",
            'email' : "Please Enter a valid email address<br><br>",
            'password' : "Please Enter password consist of 8 chars <br><br>"
        }

        error_messages = {
            'name' : {
                'required' : 'Name is required'
            },
            'email' : {
                'required' : 'Email is required'
            },
            'password' : {
                'required' : 'Password is required'
            }
        }

    