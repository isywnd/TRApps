from django import forms
from ..model.tabelDosenPengampu import DosenPengampu
from crispy_forms.helper import FormHelper

class DosenPengampuForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    class Meta:
        model = DosenPengampu
        fields = [
            "tahunAjaran",
            "dosen_Pengampu",
            "mata_kuliah",
        ]