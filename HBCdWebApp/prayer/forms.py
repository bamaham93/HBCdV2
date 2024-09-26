from django.forms import ModelForm
from prayer.models import Request


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = "__all__"
