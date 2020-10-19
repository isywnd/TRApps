from django.db import models
from.tabelDosenPengampu import DosenPengampu

class Test(models.Model):
    mata_kuliah = models.ForeignKey(DosenPengampu, on_delete=models.CASCADE)
    tanggalUjian = models.DateField()

    def __str__(self):
        return str(self.tanggalUjian)+"-"+self.mata_kuliah.mata_kuliah.namaMK