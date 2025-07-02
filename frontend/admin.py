from django.contrib import admin

from .models import User, Profile, Post


admin.site.register(User, admin.ModelAdmin)
admin.site.register(Profile, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)