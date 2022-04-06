from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    start_timestamp = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type':'datetime-local'}),
        required=True,
    )
    stop_timestamp = forms.DateTimeField(
        widget=forms.TextInput(attrs={'type':'datetime-local'}),
        required=True,
    )

    class Meta:
        model = Device
        fields = {'sensor_type','location'}
        widgets = {
            'sensor_type': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            # 'timestamp': forms.DateField(attrs={'class': 'form-control'}),
            # 'timestamp': forms.TextInput(attrs={'type':'datetime-local'}),
            # 'timestamp': forms.TextInput(attrs={'type':'datetime-local'})
            # forms.DateTimeInput(
            #     format='%d/%m/%Y %H:%M', attrs={'type': 'datetime'},
            # )

        }

    # def __init__(self, *args, **kwargs):
    #     super(DeviceForm, self).__init__(*args, **kwargs)
    #     self.fields['timestamp'].required = False
        