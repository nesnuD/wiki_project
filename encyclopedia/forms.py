from django import forms

class entryForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()