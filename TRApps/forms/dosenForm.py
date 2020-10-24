from django import forms
from ..model.tabelDosen import Dosen
from crispy_forms.helper import FormHelper

class DosenForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    class Meta:
        model = Dosen
        fields = [
            "nip_dosen",
            "nama_dosen",
        ]