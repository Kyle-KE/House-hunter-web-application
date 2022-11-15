import select
from django import forms
from django.contrib.auth.models import User
from .models import hostel

class HostelForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for key, field in self.fields.items():
    #         field.label = ""

    class Meta():
        model = hostel
        fields = '__all__'
        redirect_field_name = '/'

        labels={
            'hname':'',
            'hlocation':'',
            'haddress':'',
            'lordname':'',
            'lordcontact':'',
            'ctname':'',
            'ctcontact':'',
            'hmail':'',
            'depositamount':'',
            'rentamount':'',
            'apartment':'',
        }
        widgets = {
            'hname': forms.TextInput(attrs={'class':'float-sectionA','placeholder':'Hostel Name'}),
            'hlocation': forms.TextInput(attrs={'class':'float-sectionA' ,'placeholder':'Hostel Location'}),
            'haddress': forms.TextInput(attrs={'class':'float-sectionA' ,'placeholder':'Hostel Address'}),
            'lordname': forms.TextInput(attrs={'class':'float-sectionA' ,'placeholder':'Landlord Name'}),
            'lordcontact': forms.TextInput(attrs={'class':'float-sectionA ' ,'placeholder':'Landlord Contact'}),
            'ctname': forms.TextInput(attrs={'class':'float-sectionB', 'placeholder':'Caretaker Name'} ),
            'ctcontact': forms.TextInput(attrs={'class':'regirationForm float-sectionB', 'placeholder':'Caretaker Contact'}),
            'hmail': forms.TextInput(attrs={'class':'regirationForm float-sectionB', 'placeholder':'Email address'}),
            'depositamount': forms.TextInput(attrs={'class':'regirationForm float-sectionB', 'placeholder':'Rent'}),
            'rentamount': forms.TextInput(attrs={'class':'regirationForm float-sectionB', 'placeholder':'Deposit'}),
            'apartment': forms.TextInput(attrs={'class':'regirationForm float-sectionB', 'placeholder':'Apartment Type'}),
            'cctv': forms.TextInput(attrs={'class':''}),
            'wifi': forms.TextInput(attrs={'class':'form-control'}),
            'restaurant': forms.TextInput(attrs={'class':'form-control'}),
            'cleaning': forms.TextInput(attrs={'class':'form-control'}),
            'laundry': forms.TextInput(attrs={'class':'form-control'}),
            'gym': forms.TextInput(attrs={'class':'form-control'}),
            'elounge': forms.TextInput(attrs={'class':'form-control'}),
            'parking': forms.TextInput(attrs={'class':'form-control'}),
            'DSTV': forms.TextInput(attrs={'class':'form-control'}),
            'edescription': forms.TextInput(attrs={'class':'form-control'}),
            'himage': forms.TextInput(attrs={'class':'form-control'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')