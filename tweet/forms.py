from django import forms


class squawkForm(forms.Form):
    msg = forms.TextField(label='enter your squawk: ', max_length=140)
