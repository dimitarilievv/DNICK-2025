from django.contrib import admin
from django.template.context_processors import request

from hotelApp.models import *


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    #При креирањето на резервацијата, корисникот се доделува автоматски според најавениот
    #корисник во моментот на системот
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        room = Room.objects.filter(number=obj.room.number,is_cleaned=True).exists()
        if room and not change:
            return super(ReservationAdmin, self).save_model(request, obj, form, change)
        return

    #- Уредување/промена на резервацијата може да направи лицето што резервира,
        #рецепционер или менаџер во хотелот

    def has_change_permission(self, request, obj=None):
        if obj is None:
            return False
        return obj and obj.user==request.user and ( obj.employee.type=='r' or obj.employee.type=='m' )

    #- За резервациите се прикажува само кодот и собата
    list_display = ["code","room",]
    exclude = ["user", ]

class RoomEmployeeInline(admin.TabularInline):
    model=RoomEmployee
    extra = 0

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [RoomEmployeeInline]
    exclude = ["user", ]
    def save_model(self, request, obj, form, change):
        return super(EmployeeAdmin, self).save_model(request, obj, form, change)

class RoomAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj=None):
        #Уредување/промена на соба може да прави само хигиеничар
        return RoomEmployee.objects.filter(room=obj,
                                         employee__type = 'h',
                                         employee__user=request.user).exists()
    #а за собите се прикажува бројот и статусот на собата
    list_display = ["number","is_cleaned",]



admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Room,RoomAdmin)