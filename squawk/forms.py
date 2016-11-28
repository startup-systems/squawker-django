from django import forms


class SquawkForm(forms.Form):
    text = forms.CharField(label='Enter Squawk here', max_length=140)
