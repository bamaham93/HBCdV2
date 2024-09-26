from django.contrib import admin
from prayer.models import Request


# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    """
    """

admin.site.register(Request, RequestAdmin)