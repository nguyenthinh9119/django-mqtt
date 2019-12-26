from django.contrib import admin
# from .models import Emp
from App import models
# admin.site.register(Emp)

# Register your models here.

class AclAdmin(admin.ModelAdmin):
    search_fields = ('topic__name', )
    list_filter = ('acc', 'allow', )
    ordering = ('topic', )
    list_display = ('topic', 'allow', 'acc', 'password')


class TopicAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_filter = ('dollar', 'wildcard', )
    list_display = ('name', 'dollar', 'wildcard')


class ClientIdAdmin(admin.ModelAdmin):
    search_fields = ('name', )


admin.site.register(models.ACL, AclAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.ClientId, ClientIdAdmin)
