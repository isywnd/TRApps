
from django.db import models

class Dosen (models.Model):
    nip_dosen = models.CharField(max_length=45)
    nama_dosen = models.CharField(max_length=45)

    def __str__(self):
        return self.nama_dosen