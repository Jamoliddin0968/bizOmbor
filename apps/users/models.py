from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    phone = models.CharField(max_length=15)
    img = models.ImageField(upload_to='user/images')
    # store = models.ForeignKey('stores.Store',on_delete=models.SET_NULL,null=True,blank=True,related_name='store_workers')
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class UserTarif(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tarif = models.ForeignKey('tariff.tarif',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"{self.user.username} {self.tarif}"

class Seans(models.Model):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    user_agent = models.JSONField(null=True,blank=True)
    device_id = models.CharField(max_length=127,default="")
    is_active = models.BooleanField(default=True)
    expire_date = models.IntegerField()


