from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)