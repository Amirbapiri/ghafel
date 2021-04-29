from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django_registration.validators import (
    DUPLICATE_EMAIL,
    CaseInsensitiveUnique,
    validate_confusables_email,
)

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            User.USERNAME_FIELD,
            "password1",
            "password2",
            "full_name",
            "short_name",
        ]

        field_classes = {}

    error_css_class = "error"
    required_css_class = "required"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[User.USERNAME_FIELD].validators.extend(
            [
                validate_confusables_email,
                CaseInsensitiveUnique(
                    User,
                    User.USERNAME_FIELD,
                    DUPLICATE_EMAIL,
                )
            ]
        )
