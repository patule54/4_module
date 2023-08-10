from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description','price', 'created_date','updated_at','auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false','make_auction_as_true']
    search_fields = ['title']

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, requests, queryset):
        queryset.update(auction=False)

    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, requests, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
