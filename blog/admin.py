from django.contrib import admin
from blog.models import Author, Category, Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'categories')
    prepopulated_fields = {"slug": ("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'total_posts')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'total_posts')

admin.site.register(Post, PostAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)