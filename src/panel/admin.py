from django.contrib import admin

from .models import Server,Site,Email,Port,History, PhoneTime, WeekDay

class SiteAdmin(admin.ModelAdmin):
    list_display = ('__str__','name')
    list_filter = ('server',)

class HistoryAdmin(admin.ModelAdmin):
    list_filter = ('date','server','is_ok')

admin.site.register(WeekDay)
admin.site.register(PhoneTime)
admin.site.register(Port)
admin.site.register(Server)
admin.site.register(Site,SiteAdmin)
admin.site.register(Email)
admin.site.register(History,HistoryAdmin)