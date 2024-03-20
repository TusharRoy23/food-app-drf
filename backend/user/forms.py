from django.contrib.auth import forms, get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreationForm(forms.UserCreationForm):
    error_messages = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    # def clean_username(self):


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
