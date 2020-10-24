from django.db import models
from.tabelDosenPengampu import DosenPengampu
from.tabelMahasiswa import Mahasiswa
from.tabelTest import Test

class Scoring (models.Model):
    tanggalUjian = models.ForeignKey(Test, on_delete=models.CASCADE)
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    dosen_pengampu = models.ForeignKey(DosenPengampu, on_delete=models.CASCADE)
    hasilScore = models.IntegerField()


    def __str__(self):
        return str(self.tanggalUjian)+"-"+self.mahasiswa.nama_mahasiswa+"-"+self.dosen_pengampu.nama_dosen+"-"+self.hasilScore