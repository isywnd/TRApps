from django.db import models
from.tabelDosenPengampu import DosenPengampu
from.tabelMahasiswa import Mahasiswa

class Scoring (models.Model):
    tanggalUjian = models.DateField()
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    dosen_pengampu = models.ForeignKey(DosenPengampu, on_delete=models.CASCADE)
    hasilScore = models.IntegerField()


    def __str__(self):
        return str(self.tanggalUjian)+"-"+self.mahasiswa.nama_mahasiswa+"-"+self.dosen_pengampu.nama_dosen+"-"+self.hasilScore