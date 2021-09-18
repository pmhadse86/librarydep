from django import forms

class Subscribe(forms.Form):
        Email = forms.EmailField()

s = Subscribe()
# print(s)