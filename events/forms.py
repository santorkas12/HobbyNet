from django import forms
from django.contrib.auth import get_user_model
from .models import Event, Participant


class EventSignUpForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EventSignUpForm, self).__init__(*args, **kwargs)
        self.fields['message'] = forms.CharField(widget=forms.Textarea)
        self.fields['first_name'].disabled = True
        self.fields['last_name'].disabled = True
        self.fields['email'].disabled = True


    #first_name = forms.CharField(max_length=150)
    #last_name = forms.CharField(max_length=150)
    #email = forms.EmailField(max_length= 255)
    #message = forms.Textarea()

