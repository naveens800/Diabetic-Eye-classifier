from django.forms import ModelForm
from .models import Patient_info,imageInput

class PatientForm(ModelForm):
    
    class Meta:
        model  = Patient_info
        fields = '__all__'
        

        
class imageInputForm(ModelForm):
    
    class Meta:
        model  = imageInput
        fields = '__all__'