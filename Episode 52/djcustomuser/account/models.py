from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils import timezone
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, nama, password):
        if not email:
            raise ValueError('Pengguna harus memiliki alamat email!')

        user = self.model(
            email=self.normalize_email(email),
            nama=nama,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nama, password):
        user = self.create_user(
            email,
            password=password,
            nama=nama,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    nama = models.CharField(max_length=50)
    tmp_lahir = models.CharField(max_length=45)
    tgl_lahir = models.DateField(blank=True, default=timezone.now)
    email = models.EmailField(
        max_length=50, unique=True, verbose_name='Email Address')
    no_hp = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nama',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.email.split('@')[0]
