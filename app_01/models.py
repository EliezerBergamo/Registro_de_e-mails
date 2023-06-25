# Imports

from django.db import models

# Parâmetros da tabela (SQL) e como devem ser preenchidos


class User(models.Model):
    email = models.CharField(max_length=254, unique=True)
