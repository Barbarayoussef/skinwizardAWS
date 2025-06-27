# Register your models here.
from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',  'is_available', 'created_at')
    search_fields = ('name','price')
    list_filter = ('is_available',)
