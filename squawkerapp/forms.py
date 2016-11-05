from django import forms


class squawkerAppForm(forms.Form):
    msg = forms.CharField(label='Please enter your Squawk', max_length=140)
