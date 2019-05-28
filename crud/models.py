from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=120)
    quantity = models.IntegerField()
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organic = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title