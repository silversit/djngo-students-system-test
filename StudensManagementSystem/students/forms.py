from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'email', 'msg']



    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        for myField in self.fields :
            self.fields[myField].widget.attrs['class'] = 'form-control'
