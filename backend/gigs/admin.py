from django.contrib import admin
from .models import Gig

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'delivery_time', 'owner', 'created_at')
    search_fields = ('title', 'category', 'owner__username')
    list_filter = ('category',)
