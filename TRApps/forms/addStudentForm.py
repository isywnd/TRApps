from django import forms
from ..model.tabelMahasiswa import Mahasiswa

class mahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = [
            "nim",
            "nama_mahasiswa",
        ]