from django.db import models


# Create your models here.
class Request(models.Model):
    """
    """
    REQUEST_CATEGORY_CHOICES = [
        ("HE", "Health"),
        ("FI", "Financial"),
        ("FA", "Family"),
        ("SP", "Spiritual"),
        ("OT", "Other"),
    ]

    first_name = models.CharField(max_length=100, null=True, blank=True,)
    last_name = models.CharField(max_length=100, null=True, blank=True,)
    category = models.CharField(max_length=2, choices=REQUEST_CATEGORY_CHOICES)
    description = models.TextField(max_length=5000, null=True, blank=True,)
    is_answered = models.BooleanField(default=False, null=True, blank=True,)
    answer = models.TextField(null=True, blank=True,)

    def __str__(self):
        """
        :return:
        """
        return f"{self.first_name} {self.last_name}"
