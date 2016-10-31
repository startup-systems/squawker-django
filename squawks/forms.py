from django import forms


class SquawkForm(forms.Form):
    squawk_text = forms.CharField(label='squawk_text', max_length=140)
