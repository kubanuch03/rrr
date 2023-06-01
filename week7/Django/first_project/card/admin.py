from django.contrib import admin
from .models import Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title','id','created_at','updated_at')
    search_fields = ('id','title',)

