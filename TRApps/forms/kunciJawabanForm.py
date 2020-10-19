from django import forms
from ..model.tabelKunciJawaban import KunciJawaban
from ..model.tabelTest import Test
from ..model.tabelDosenPengampu import DosenPengampu

class kunciJawabanForm(forms.ModelForm):
    tanggalUjian = forms.ModelChoiceField(queryset=Test.objects.all(), widget=forms.HiddenInput())
    mata_kuliah = forms.ModelChoiceField(queryset=DosenPengampu.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = KunciJawaban
        fields = [
            "tanggalUjian",
            "mata_kuliah",
            "jawaban",
            "point",
        ]