from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='名前',max_length=10)
    email = forms.EmailField(label='メールアドレス')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)
   