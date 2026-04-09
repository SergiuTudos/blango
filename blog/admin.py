from django.contrib import admin
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')
    
# Register your models here.
from blog.models import Tag, Post
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

