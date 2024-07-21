from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book, Author
class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author']#liked_by


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields = '__all__'