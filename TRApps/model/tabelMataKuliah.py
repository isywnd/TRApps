
from django.db import models

class MataKuliah (models.Model):
    kodeMK = models.CharField(max_length=10)
    namaMK = models.CharField(max_length=45)

    def __str__(self):
        return self.namaMK