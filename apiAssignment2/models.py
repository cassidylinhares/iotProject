from django.db import models


class Moisture(models.Model):
    plant_id = models.CharField(
        default='plant1', blank=False, null=False, max_length=10)
    level = models.IntegerField(default=25, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    plant_type = models.CharField(blank=False, null=False, max_length=20)

    def __str__(self):
        return self.created + " plant id: " + self.plant_id + " moisture: " + self.level + " name: " + self.name + ' plant type: ' + self.plant_type
