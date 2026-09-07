from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    # Allow blank and null values so Django doesn't crash if a file goes missing
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name