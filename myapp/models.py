# myapp/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    # Standard Django FileSystemStorage (no storage parameter needed)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.name or f"Item {self.id}"