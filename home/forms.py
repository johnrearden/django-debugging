from django.forms import ModelForm


class PersonForm(ModelForm):

    class Meta:
        fields = '__all__'
        widgets={
            'date_of_birth': forms.DateInput(attrs={
                'type': 'datetime-local',
                
            }),
        }