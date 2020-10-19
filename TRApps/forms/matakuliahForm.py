from django import forms
from ..model.tabelMataKuliah import MataKuliah

class mkForm(forms.ModelForm):
    class Meta:
        model = MataKuliah
        fields = [
            "kodeMK",
            "namaMK",
        ]