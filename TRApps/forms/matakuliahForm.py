from django import forms
from ..model.tabelMataKuliah import MataKuliah
from crispy_forms.helper import FormHelper

class mkForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    class Meta:
        model = MataKuliah
        fields = [
            "kodeMK",
            "namaMK",
        ]