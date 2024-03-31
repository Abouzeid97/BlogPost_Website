from django.contrib import admin
from .models import Author, Post, Tag, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
     prepopulated_fields = {"slug": ("title",)}
     list_filter = ("author", "tag", "time_posted",)
     list_display = ("id","title", "time_posted", "author",)

     



admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)