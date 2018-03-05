from django.contrib.auth.base_user import BaseUserManager

class ProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password):
        username = self.model(username)
        user = self.model(username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password,**extra_fields) :
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password)
