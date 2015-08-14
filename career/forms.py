from django import forms

class LinkForm(forms.Form):
    link = forms.URLField(label='LinkedIn', max_length=200, required = True, widget=forms.TextInput(attrs={'class':'special', 'size': '40'}))