from django import forms
from ..model.tabelKunciJawaban import KunciJawaban
from ..model.tabelTest import Test
from ..model.tabelDosenPengampu import DosenPengampu
from crispy_forms.helper import FormHelper

class kunciJawabanForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
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