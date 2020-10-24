from django import forms
from ..model.tabelTest import Test
from crispy_forms.helper import FormHelper

class testForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    class Meta:
        model = Test
        fields = [
            "mata_kuliah",
            "tanggalUjian",
        ]