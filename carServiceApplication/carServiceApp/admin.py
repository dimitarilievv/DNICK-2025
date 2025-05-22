from django.contrib import admin

from carServiceApp.models import ServicePlaceManufacturer, ServicePlace, Service, Manufacturer, Car


# Register your models here.
# vo rabotilnica inline za m-m relacija
class ServicePlaceManufacturerInline(admin.TabularInline):
    model=ServicePlaceManufacturer
    extra = 0


class ServicePlaceAdmin(admin.ModelAdmin):
    inlines = [ServicePlaceManufacturerInline,]
    def has_delete_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False


class ServiceAdmin(admin.ModelAdmin):
    exclude = ["user",]
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        return super(ServiceAdmin,self).save_model(request, obj, form, change)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name",]

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

class CarAdmin(admin.ModelAdmin):
    list_display = ["type","max_speed",]

admin.site.register(ServicePlace,ServicePlaceAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
admin.site.register(Car,CarAdmin)
admin.site.register(ServicePlaceManufacturer)
