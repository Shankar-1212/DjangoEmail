from django import forms

class EmailForm(forms.Form):
    name= forms.CharField()
    subject= forms.CharField()
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
