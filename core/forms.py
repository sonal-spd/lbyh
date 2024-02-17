from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from .models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField


class SignUpForm(UserCreationForm):
    # username = forms.CharField(label="",
    #                            max_length=32, help_text="<small id='emailHelp' class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    # name = forms.CharField(label="",
    #                              max_length=32, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    
    # phone = PhoneNumberField(label="",
    #                              widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}))
    # email = forms.EmailField(label="",
    #                          max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    # password1 = forms.CharField(label="", help_text="<small><ul class='form-text text-muted'><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>",
    #                             max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    # password2 = forms.CharField(label="", help_text="<small class='form-text text-muted'>Enter the same password as before, for verification.</small>",
    #                             max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'name','phone','email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    # username = forms.CharField(label="Username:",
    #                            max_length=32, help_text="<small id='emailHelp' class='form-text text-muted'>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>", widget=forms.TextInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(label="Name:",
    #                              max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # phone = PhoneNumberField(label="Phone Number:",
    #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(label="Email",
    #                          max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(label="",
    #                            max_length=50, widget=forms.PasswordInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ['username', 'name','phone','email']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Old password:",
                                   max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="New password:", help_text="<small><ul class='form-text text-muted'><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>",
                                    max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="New password confirmation:",
                                    max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User