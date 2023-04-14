from django import forms
from testapp.models import Student
class StudentForm(forms.ModelForm):
    def clean_marks(self):
        inputmarks=self.cleaned_data['marks']
        if inputmarks < 40 :
            raise forms.ValidationError('Marks must be more or equal to 40')
        return inputmarks
    class Meta:
        model=Student
        fields='__all__'
