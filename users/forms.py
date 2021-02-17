from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'date_of_birth',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'date_of_birth',)



import datetime
from django import forms
from allauth.account.forms import SignupForm

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=150, label= 'First Name')
    last_name = forms.CharField(max_length=150, label= 'Last Name')
    #date_of_birth = forms.DateField(initial=datetime.date.today,label= 'Date of Birth')

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user