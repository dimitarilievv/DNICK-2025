from django.contrib import admin

from FlightApp.models import Airline, Pilot, Flight, Balloon, AirlinePilot


# Register your models here.

class AirlinePilotInline(admin.TabularInline):
    model = AirlinePilot
    extra = 0

class AirlineAdmin(admin.ModelAdmin):
    list_display = ("name","year_founded","outside_Europe")
    inlines = [AirlinePilotInline, ]
    # def has_add_permission(self, request):
    #     return False

class PilotAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name")

class FlightAdmin(admin.ModelAdmin):
    list_display = ("code", "take_off_airport","landing_airport","user")
    exclude = ("user",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)
    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Balloon)