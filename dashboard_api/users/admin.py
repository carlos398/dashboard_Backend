from django.contrib import admin

from users import models

admin.site.register(models.UserProfile)
admin.site.register(models.UsersTests)
