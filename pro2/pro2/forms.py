from django import forms
from app2.models import Document

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document','department','image','type' )
