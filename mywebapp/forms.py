from django import forms


class squawkerForm(forms.Form):
    msg = forms.CharField(label='Enter your Squawk', max_length=140)
