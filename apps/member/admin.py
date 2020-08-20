from django.contrib import admin
from .models import DevconMember, Speaker, Prospect

class DevconMemberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'company', 'designation', 'date_created')
    readonly_fields = ('uuid', 'email', 'name', 'phone', 'company', 'designation', 'date_created')


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone', 'company', 'designation', 'topic', 'topic_desc', 'date_created')
    readonly_fields = ('uuid', 'email', 'name', 'phone', 'company', 'designation', 'topic', 'topic_desc', 'date_created')

class ProspectAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_created')
    readonly_fields = ('uuid', 'email', 'date_created')

admin.site.register(DevconMember, DevconMemberAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Prospect, ProspectAdmin)

