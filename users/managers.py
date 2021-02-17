from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, date_of_birth, password):
        if not email:
            raise ValueError(_("The email must be set"))

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, date_of_birth, password):

        user = self.create_user(
            email=email,
            password = password,
            first_name = first_name,
            last_name = last_name,
            date_of_birth = date_of_birth,
        )

        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user