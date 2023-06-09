from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from app.managers import CustomAccountManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    # these fields will be prompted when creating a super user using CustomUser model
    REQUIRED_FIELDS = ['username', 'first_name']

    objects = CustomAccountManager()

    def __str__(self):
        return "%s %s" % (self.username, self.email)

    class Meta:
        ordering = ['-created_at']
        db_table = 'tUser'
        indexes = [
            models.Index(fields=['email', 'username']),
        ]
