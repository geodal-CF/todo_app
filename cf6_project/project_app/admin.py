from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.To_do)   # This allows the superuser to create, view, edit and delete to-dos through the admin panel.