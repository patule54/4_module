from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description','price', 'created_at','auction']
    list_filter = ['auction', 'created_at']

admin.site.register(Advertisement, AdvertisementAdmin)
