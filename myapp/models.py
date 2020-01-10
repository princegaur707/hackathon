from django.db import models

# Create your models here.
class UserFeedBack(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
