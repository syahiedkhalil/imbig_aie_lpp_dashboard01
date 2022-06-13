from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
	class RolesEnum(models.TextChoices):
	    ADMIN = 'admin'
	    OPERATOR = 'operator'
	    QC = 'qc'

	roles = models.CharField(max_length=255, choices=RolesEnum.choices, default=RolesEnum.ADMIN)

	class Meta:
		# managed = False
		db_table = 'auth_user'