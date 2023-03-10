from django.db import models
# from password_manager.login.models import User
from django.contrib.auth.models import User

class Site(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.CharField(max_length=100, primary_key=True)

class SavedPassword(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    site = models.ForeignKey(Site, on_delete=models.PROTECT) # si elimino un site raisea error y tengo que eliminar todo las pass asociadas
    user = models.ForeignKey(User, on_delete=models.CASCADE) # si elimino el user elimina sus saved passowrds. OK
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

