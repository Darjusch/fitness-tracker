from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Training


# Example of Form
# class AddTrainingForm(forms.Form):
#     benchpress = forms.IntegerField(label='benchpress', max_value=200, min_value=20)
#     squats = forms.IntegerField(label='squats', max_value=250, min_value=20)
#     deadlift = forms.IntegerField(label='deadlift', max_value=300, min_value=20)
#     militarypress = forms.IntegerField(label='militarypress', max_value=100, min_value=5)
#     pullups = forms.IntegerField(label='pullups', max_value=30, min_value=1)

#Example of ModelForm
class AddTrainingForm(ModelForm):
    class Meta:
        model = Training
        fields = ['date', 'bench', 'squats', 'pullups', 'deadlift', 'militarypress']
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }