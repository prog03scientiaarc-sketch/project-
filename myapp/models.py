from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        # Always return a plain string; avoid referencing self.image.url here
        return self.name or f"Item {self.id}"