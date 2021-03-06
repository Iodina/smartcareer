from django import forms
from djtokeninput import TokenField
from career.models import Skill

class LinkForm(forms.Form):
    link = forms.URLField(label='LinkedIn', max_length=200, widget=forms.TextInput(attrs={'class':'special', 'size': '44'}), required=False)

class TokenForm(forms.Form):
    Skills = TokenField(Skill, required=False)

class ProfForm(forms.Form):
    prof = forms.CharField(label='Profession', max_length=200, widget=forms.TextInput(attrs={'class':'special', 'size': '44'}))