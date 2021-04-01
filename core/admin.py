from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Board, Rubric


# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_photo', 'content', 'price', 'published_data', 'rubric')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('rubric',)
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '---'

    get_photo.short_description = 'Фото'


admin.site.register(Board, BoardAdmin)
admin.site.register(Rubric)
