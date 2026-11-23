from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        help_text="Required. Enter a valid, unique email address."
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")


# NEW: Form for updating User fields
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


# NEW: Form for updating Profile fields
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("pf_picture", "bio", "status")