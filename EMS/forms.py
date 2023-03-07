from django import forms
from django.forms import ModelForm
from .models import Employee
from .widget import DatePickerInput 
from  datetime import datetime




class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ('leave_count',)
        widgets = {
            'date_of_birth': DatePickerInput(),
            'date_of_joining': DatePickerInput(),
        }
    def clean(self):
        cleaned_data = super().clean()
        date_of_birth=cleaned_data.get("date_of_birth")
        date_of_joining=cleaned_data.get("date_of_joining")
        check_days=(date_of_joining-date_of_birth).days
        date_object = datetime.now().date()
        if date_of_birth<date_object:
            if check_days>365*18:
                return cleaned_data
            else:
                raise forms.ValidationError("Employee age must be greater than 18 years .")
        else:
            raise forms.ValidationError(" Date of birth cannot be in future .")
    def clean_zipcode(self):
        zipcode=self.cleaned_data.get('zipcode')
        if zipcode <0:
            raise forms.ValidationError("Zipcode cannot be negative .")
        else:
            return zipcode
            
        


        


    # def clean_date_of_birth(self):
    #     date_of_birth=self.cleaned_data.get("date_of_birth")
    #     date_of_joining=self.cleaned_data.get("date_of_joining")
    #     date_object = datetime.now().date()
    #     if date_of_birth>date_object:
    #         raise forms.ValidationError("Date of birth cannot be in future .")
    #     else:
    #         return date_of_birth
    # def clean_date_of_joining(self):
    #         date_of_birth=self.cleaned_data.get("date_of_birth")
    #         date_of_joining=self.cleaned_data.get("date_of_joining")
    #         check_days=(date_of_joining-date_of_birth).days
    #         if check_days >=365*18:
    #             return date_of_joining
    #         else:
    #             raise forms.ValidationError("Employee age must be greater than 18 years .")





