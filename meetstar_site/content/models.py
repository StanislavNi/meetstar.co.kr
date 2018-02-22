from django.db import models

class Videos(models.Model):
    address = models.URLField(null=False)

    def __str__(self):
        return self.address
