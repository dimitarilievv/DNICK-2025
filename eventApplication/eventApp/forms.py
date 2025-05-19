from eventApp.models import Event
from django import forms

class EventForm(forms.ModelForm):
    bands = forms.CharField(
        label='Bands (comma-separated)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )

    def __init__(self, *args ,**kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Event
        fields = ["name", "datetime", "poster", "is_closed"]
        widgets = {
            'datetime': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            )
        }