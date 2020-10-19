from django.db import models
from .tabelTest import Test
from .tabelDosenPengampu import DosenPengampu

class KunciJawaban (models.Model):
    tanggalUjian = models.ForeignKey(Test, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(DosenPengampu, on_delete=models.CASCADE)
    jawaban = models.CharField(max_length=45)
    point = models.IntegerField()

    def __str__(self):
        return str(self.tanggalUjian.tanggal_ujian)+"-"+self.mata_kuliah.namaMK+"-"+self.jawaban+"-"+self.point