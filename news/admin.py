from django.contrib import admin
from .models import User, New


@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'status')
    list_filter = ('status', 'created')


# Register your models here.
admin.site.register(User)
admin.site.register(News)
