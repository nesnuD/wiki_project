from django import forms

class entryForm(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(label="content")

class editbtnForm(forms.Form):
    button = forms.BooleanField(label="Edit", required="False")