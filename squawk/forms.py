from django import forms
from squawk import models


class SquawkForm(forms.Form):
    text = forms.CharField(label='Squawk', max_length=140)
    # class Meta:
    #     model = models.Squawk
    #     widgets = {
    #         'content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
    #     }
