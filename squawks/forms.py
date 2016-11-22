from django import forms


class SquawkForm(forms.Form):
    squawk_line = forms.CharField(label='squawk_line', max_length=140)
