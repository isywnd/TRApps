from django import forms
from ..model.tabelMahasiswa import Mahasiswa
from crispy_forms.helper import FormHelper


class mahasiswaForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Mahasiswa
        fields = [
            "nim",
            "nama_mahasiswa",
        ]