from django.db import models

class Moisture(models.Model):
    level = models.IntegerField(default=50, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created + " moisture: " + self.level
