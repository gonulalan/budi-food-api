from django.contrib import admin
from users_api import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.UserFeedItem)
admin.site.register(models.Platform)
