from django.contrib import admin
from .models import Post, Comment
from django.contrib.auth.models import Group


admin.site.register(Comment)
admin.site.unregister(Group)
admin.site.site_header = "Creative Blog Admin Panel"
admin.site.site_title = "Creative Blog Admin"


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'last_update')
    list_filter = ('author', 'created_at', 'last_update')

admin.site.register(Post, PostAdmin)