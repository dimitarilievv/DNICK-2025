from django.contrib import admin

from eventApp.models import EventBand, Event, Band


# Register your models here.
class EventBandInline(admin.TabularInline):
    model = EventBand
    extra = 0

class EventAdmin(admin.ModelAdmin):
    inlines = [EventBandInline, ]
    exclude = ["user",]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Event, EventAdmin)
admin.site.register(Band)
admin.site.register(EventBand)

