from django import forms
from .models import Squawk

class SquawkForm(forms.ModelForm):

    class Meta:
        model = Squawk
        fields = ('text',)
