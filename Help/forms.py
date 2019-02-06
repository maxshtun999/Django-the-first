from django import forms

from .models import Help

class HelpForm(forms.ModelForm):

    class Meta:
        model = Help
        fields = ('first_name', 'last_name', 'e_mail', 'text')
