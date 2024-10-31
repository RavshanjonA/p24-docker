from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db.models import EmailField, BooleanField, ImageField
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext_lazy as _

from core.managers import AccountManager
from core.tasks import resize_image_task


def image_size_validators(file):
    if file.size >= 4 * 1024 * 1024:
        raise ValidationError(_("Image size must be less than 4 mb"))


class Account(AbstractBaseUser, PermissionsMixin):
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    email = EmailField(unique=True)
    avatar = ImageField(upload_to="avatars",
                        validators=[FileExtensionValidator(allowed_extensions=["jpg", 'jpeg', 'png'],
                                                           message=_("Image type must be like: jpg, png, jpeg")),
                                    image_size_validators],
                        default="avatar_docker.jpeg"
                        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resize_image_task.delay(self.id)

    USERNAME_FIELD = 'email'
    objects = AccountManager()
