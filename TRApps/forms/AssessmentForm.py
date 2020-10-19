# import the standard Django Forms
# from built-in library
from django import forms
from ..model.tabelAssessment import Assessment


# creating a form
class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = [
            'file',
            'score',
        ]
