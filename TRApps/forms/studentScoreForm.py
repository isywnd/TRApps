from django import forms
from ..model.tabelScoring import Scoring
from ..model.tabelTest import Test
from ..model.tabelDosenPengampu import DosenPengampu

class ScoreStudentForm(forms.ModelForm):
    tanggalUjian = forms.ModelChoiceField(queryset=Test.objects.all(), widget=forms.HiddenInput())
    dosen_pengampu = forms.ModelChoiceField(queryset=DosenPengampu.objects.all(), widget=forms.HiddenInput())
    hasilScore = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Scoring
        fields = [
            "tanggalUjian",
            "mahasiswa",
            "dosen_pengampu",
            "hasilScore",
        ]