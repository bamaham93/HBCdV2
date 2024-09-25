from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # category drop down
    short_description = forms.CharField(max_length=100)
    prayer_request = forms.CharField(widget=forms.Textarea)

    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)