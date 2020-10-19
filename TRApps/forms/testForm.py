from django import forms
from ..model.tabelTest import Test

class testForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            "mata_kuliah",
            "tanggalUjian",
        ]