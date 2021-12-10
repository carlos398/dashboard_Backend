from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from datetime import datetime


class UserProfileManeger(BaseUserManager):
    """ Manager para perfiles del usuario """

    def create_user(self, email, name, last_name, password=None):
        """ Crear un nuevo perfil de usuario """
        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, email, name, last_name, password):
        user = self.create_user(email, name, last_name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo base de datos para Usuarios en el sistema """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=datetime.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManeger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name']


    def get_full_name(self):
        """Retorna el nombre completo del usuario"""
        return(f"{self.name} {self.las_name}")


    def get_short_name(self):
        """Retorna el nombre corto del usuario"""
        return self.name

    
    def str(self):
        """Retorna cadena represtando al usuario"""
        return self.email


class UsersTests(models.Model):
    """ Model para almacenar las respuestas de los usuarios """

    user_id = models.IntegerField()
    question_1 = models.BooleanField(default=None)
    question_2 = models.BooleanField(default=None)
    question_3 = models.BooleanField(default=None)
    question_4 = models.BooleanField(default=None)
    question_5 = models.BooleanField(default=None)

    REQUIRED_FIELDS = ['user_id']
