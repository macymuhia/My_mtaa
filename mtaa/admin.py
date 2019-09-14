from django.contrib import admin
from .models import Admin, NeighbourHood, Business

# Register your models here.

admin.site.register(Admin)
admin.site.register(NeighbourHood)
admin.site.register(Business)

