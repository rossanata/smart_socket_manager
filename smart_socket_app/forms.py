from django import forms
from django.forms import Textarea

from smart_socket_app.models import SmartSocket


class SmartSocketForm(forms.ModelForm):
    class Meta:
        model = SmartSocket
        fields = ('name', 'description')
        widgets = {
          'description': Textarea(attrs={'rows': 5, 'cols': 20}),
        }
