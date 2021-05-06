from django.contrib import admin
from board.models import *


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'date_created', 'is_deleted', 'column')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_deleted',)
    list_filter = ('column', 'date_created', 'is_deleted')


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_created')
    list_display_links = ('id', 'name')
    search_fields = ('name',)



admin.site.register(Note, BoardAdmin)
admin.site.register(Column, ColumnAdmin)
