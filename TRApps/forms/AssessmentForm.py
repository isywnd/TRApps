# import the standard Django Forms
# from built-in library
from django import forms
from ..model.tabelAssessment import Assessment
from crispy_forms.helper import FormHelper


# creating a form
class AssessmentForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    class Meta:
        model = Assessment
        fields = [
            'file',
            'score',
        ]
