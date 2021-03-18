from django.contrib import admin
from .models import Post,Comment
# Register your models here.

#admin.site.register(models.Post)
#admin.site.register(models.Comment)

#@admin.register(Comment)
#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('user', 'message', 'post', 'created_at', 'active')
#    list_filter = ('active', 'created_at')
#    search_fields = ('user', 'message')
#    actions = ['approve_comments']

#    def approve_comments(self, request, queryset):
#        queryset.update(active=True)
