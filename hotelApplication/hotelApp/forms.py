from django import forms

from hotelApp.models import Reservation


class ReservationForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ReservationForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget,forms.CheckboxInput):
                field.widget.attrs['class']='form-control'

    class Meta:
        model=Reservation
        fields='__all__'
        exclude=["user",]
        widgets={
            'date_start':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'date_end':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }
