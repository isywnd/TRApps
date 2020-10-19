from django import forms
from ..model.tabelDosenPengampu import DosenPengampu

class DosenPengampuForm(forms.ModelForm):
    class Meta:
        model = DosenPengampu
        fields = [
            "tahunAjaran",
            "dosen_Pengampu",
            "mata_kuliah",
        ]