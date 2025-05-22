from django import forms

from carServiceApp.models import Service


class ServiceForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ServiceForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget,forms.CheckboxInput):
                field.widget.attrs['class']='form-control'
    class Meta:
        model=Service
        fields="__all__"
        exclude=["user",]
        widgets={
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }