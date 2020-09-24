from django.contrib import admin
from blog.models import Blog, Contact


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("my_styles.css",)
        }
        js = ("my_code.js",)


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
