from django import forms


class SquawkForm(forms.Form):
    text = forms.CharField(label='Get Squawking :', max_length=140)
