from django.db import models

# Create your models here.
class Story(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    file = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.name