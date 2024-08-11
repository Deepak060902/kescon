from django import forms

class ReturnForm(forms.Form):
    reason = forms.CharField(widget=forms.Textarea, label='Reason for Return')
