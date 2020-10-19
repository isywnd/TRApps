from django.db import models

class Mahasiswa (models.Model):
    nim = models.CharField(max_length=12)
    nama_mahasiswa = models.CharField(max_length=45)

    def __str__(self):
        return self.nama_mahasiswa