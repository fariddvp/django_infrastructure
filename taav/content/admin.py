from django.contrib import admin

# Register your models here.
from content.models import Post, PostMedia, Tag
from location.models import Location

admin.site.register(Post)
admin.site.register(PostMedia)
admin.site.register(Tag)
admin.site.register(Location)