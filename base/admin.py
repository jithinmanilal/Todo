from django.contrib import admin
from .models import Task
from . import models
import django.apps
# Register your models here.

admin.site.register(Task)