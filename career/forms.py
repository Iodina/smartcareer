from django import forms

class LinkForm(forms.Form):
    link = forms.CharField(label='LinkedIn', max_length=100, required = True)