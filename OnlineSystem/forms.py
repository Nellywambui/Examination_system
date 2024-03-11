from django import forms
from OnlineSystem.models import Contact
from django import forms
from OnlineSystem.models import Registration, Students

class StudentForm(forms.Form):
    name = forms. CharField(label='Enter your name',max_length=50, required=True)
    age = forms .IntegerField(min_value=18, label='enter your age', required=True)
    check = forms.BooleanField(label='Do you want to join', required=True)
    category = forms.ChoiceField(choices=[('Student', 'Student'), ('Parent', 'Parent'), ('Teacher', 'Teacher')])


class StudentComplains(forms.ModelForm):
    class Meta:
            model = Contact
            fields = ['name', 'email', 'message']


class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password']


class StudentForm1(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['first_name', 'last_name', 'age', 'date_of_birth']
