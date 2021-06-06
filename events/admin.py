from events.models import Business, Neighborhood, Profile
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)

admin.site.register(Neighborhood)

admin.site.register(Business)