from django.contrib import admin

# Register your models here.
from boot_app.models import Puppy, Owner

admin.site.register(Puppy)
admin.site.register(Owner)