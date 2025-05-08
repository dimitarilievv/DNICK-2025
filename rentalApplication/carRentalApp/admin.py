from django.contrib import admin
from .models import *

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    readonly_fields = ("user",)

    def get_queryset(self, request):
        return Manufacturer.objects.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(ManufacturerAdmin, self).save_model(request, obj, form, change)


admin.site.register(Car,CarAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
