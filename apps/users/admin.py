from django.contrib import admin


from .models import Worker,Manager,User

admin.site.register([Worker,Manager,User])