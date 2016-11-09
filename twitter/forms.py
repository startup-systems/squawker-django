from django import forms


class squawkForm(forms.Form):
    msg = forms.CharField(label='Enter Msg:', max_length=140)
