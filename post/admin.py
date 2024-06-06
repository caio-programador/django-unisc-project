from django.contrib import admin

from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'isVisible')
    list_editable = ('isVisible',)

admin.site.register(models.Post, PostAdmin)
