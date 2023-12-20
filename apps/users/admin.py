from django.contrib import admin


from .models import Worker,Manager

admin.site.register([Worker,Manager])