from django import forms


class SquawkForm(forms.Form):
    text = forms.CharField(label='Squawk', max_length=140)
