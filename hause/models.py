from django.db import models

class HauseModel(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
