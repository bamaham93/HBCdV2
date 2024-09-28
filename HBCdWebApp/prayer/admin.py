from django.contrib import admin
from prayer.models import Request


# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    """
    """
    # fields = ['first_name', 'last_name', 'category']  # Change the field within the Django admin panel.
    list_filter = ['first_name', 'last_name', 'category',
                   'is_answered']  # Change the fields that can be sorted by in the Django admin table.
    list_display = ['first_name', 'last_name', 'category',
                    'is_answered']  # Changes the field displayed in the Requests admin table.


admin.site.register(Request, RequestAdmin)
