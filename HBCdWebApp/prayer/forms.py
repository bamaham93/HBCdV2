from django.forms import ModelForm, forms
from prayer.models import Request


class RequestForm(ModelForm):
    class Meta:
        model = Request
        # sumbit = forms.forms
        fields = "__all__"
