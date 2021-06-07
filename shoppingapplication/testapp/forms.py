from django import forms
from testapp.models import goods
from django.contrib.auth.models import User
class goods_modelform(forms.ModelForm):
    class Meta:
        model=goods
        fields="__all__"
class signup_modelform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email"]
