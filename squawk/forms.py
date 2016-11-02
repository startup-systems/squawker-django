from django import forms

class SquawkForm(forms.Form):
    message = forms.CharField(label='Message', max_length=140)
