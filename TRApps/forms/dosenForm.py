from django import forms
from ..model.tabelDosen import Dosen

class DosenForm(forms.ModelForm):
    class Meta:
        model = Dosen
        fields = [
            "nip_dosen",
            "nama_dosen",
        ]