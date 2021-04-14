from django.contrib import admin
from .models import Post, Category
# Register your models here.

# admin.site.register(Post)
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "post_date", "category")
	ordering = ("-post_date",)
	search_fields = ("title", "body")
	empty_value_display = '→→→empty→→→'