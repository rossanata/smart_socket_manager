from django import forms

from smart_socket_app.models import LogInProfile


class LogInForm(forms.ModelForm):

    class Meta:
        model = LogInProfile
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
