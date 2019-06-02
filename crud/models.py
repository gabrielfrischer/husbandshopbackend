from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=120)
    quantity = models.IntegerField(default=1)
    description = models.TextField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    organic = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title