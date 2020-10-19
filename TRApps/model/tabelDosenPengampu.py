from django.db import models
from.tabelDosen import Dosen
from.tabelMataKuliah import MataKuliah

class DosenPengampu (models.Model):
    tahunAjaran = models.CharField(max_length=45)
    dosen_Pengampu = models.ForeignKey(Dosen, on_delete=models.CASCADE)
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)

    def __str__(self):
        return self.dosen_Pengampu.nama_dosen+"-"+self.mata_kuliah.namaMK+"-"+self.tahunAjaran