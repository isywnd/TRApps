from django import forms
from ..model.tabelScoring import Scoring
from ..model.tabelTest import Test
from ..model.tabelDosenPengampu import DosenPengampu
from crispy_forms.helper import FormHelper

class ScoreStudentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    tanggalUjian = forms.ModelChoiceField(queryset=Test.objects.all(), widget=forms.HiddenInput())
    dosen_pengampu = forms.ModelChoiceField(queryset=DosenPengampu.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = Scoring
        fields = [
            "tanggalUjian",
            "mahasiswa",
            "dosen_pengampu",
        ]