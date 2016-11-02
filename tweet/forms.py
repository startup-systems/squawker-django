from django import forms


class squawkForm(forms.Form):
    message = forms.CharField(label='enter your squawk: ', max_length=140)
