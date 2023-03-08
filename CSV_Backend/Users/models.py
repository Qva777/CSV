import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from CSV_Backend.Users.validators import validate_password


class MyUser(AbstractUser):
    """ Clients models/fields """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(verbose_name='Username', db_index=True, unique=True, max_length=64, blank=False)
    password = models.CharField(validators=[validate_password], verbose_name='Password', max_length=88, blank=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', ]

    def __str__(self):
        """ String representation """
        return self.username

    class Meta:
        """ Representation in admin panel """
        verbose_name = 'User'
        verbose_name_plural = 'Users'
