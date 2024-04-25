from django.contrib import admin
from .models import UserAccount
# Register your models here.
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name')
    list_display_links = ('id', 'email', )
    search_fields = ('name',)
    

admin.site.register(UserAccount, BlogPostAdmin)
