from django.contrib import admin
# from learning_logs.models import Topic
# from .models import Topic
from . import models

# Register your models here.
admin.site.register(models.Topic)
admin.site.register(models.Entry)
