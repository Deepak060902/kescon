from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import KesconUser, Address

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = KesconUser
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'e_mail', 'city', 'state', 'postal_code', 'country')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = KesconUser
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'e_mail', 'city', 'state', 'postal_code', 'country')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'postal_code', 'country', 'address_type']
