from django import forms


class squawkForm(forms.Form):
    msg = forms.CharField(label='enter your squawk: ', max_length=140)
