from datetime import datetime

from django.contrib import admin

from realEstateApp.models import RealEstateAgent, RealEstateCharacteristic, Agent, RealEstate, Characteristic


# Register your models here.
class RealEstateAgentInline(admin.TabularInline):
    model=RealEstateAgent
    extra=0
class RealEstateCharacteristicInline(admin.TabularInline):
    model = RealEstateCharacteristic
    extra = 0

class RealEstateAdmin(admin.ModelAdmin):
    inlines = [RealEstateAgentInline,RealEstateCharacteristicInline,]
    list_display = ("name","area","description",)

    #Огласи за продажба може да бидат додадени само од агенти
    def has_add_permission(self, request):
        return Agent.objects.filter(user=request.user).exists()
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # и по автоматизам агентот кој додава оглас е еден од задолжените за продажба на таа недвижност
        if not change:
            RealEstateAgent.objects.create(real_estate=obj,agent=Agent.objects.filter(user=request.user).first())

    #Еден оглас може да биде избришан само ако нема додадено ниту една карактеристика која го опишува
    def has_delete_permission(self, request, obj=None):
        return not RealEstateCharacteristic.objects.filter(real_estate=obj).exists()

    #Огласите можат да бидат менувани само од агенти кои се задолжени за продажба на тој оглас,
    def has_change_permission(self, request, obj=None):
        # return RealEstateAgent.objects.filter(real_estate=obj,agent=Agent.objects.filter(user=request.user).first()).exists()
        return obj and RealEstateAgent.objects.filter(real_estate=obj,agent__user=request.user).exists()

    #останатите агенги може само да ги гледаат тие огласи
    def has_view_permission(self, request, obj=None):
        return True

    #На супер-корисниците во Админ панелот им се прикажуваат само огласите кои се објавени на денешен датум
    def get_queryset(self, request):
        if request.user.is_superuser:
            return RealEstate.objects.filter(date=datetime.now().date())
        return RealEstate.objects.all()



class AgentAdmin(admin.ModelAdmin):
    exclude = ["user",]
    list_display = ("name","surname",)
    def has_add_permission(self, request):
        return request.user.is_superuser
    def save_model(self, request, obj, form, change):
        obj.user=request.user
        super().save_model(request, obj, form, change)

class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ("name",)
    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Agent,AgentAdmin)
admin.site.register(RealEstate,RealEstateAdmin)
admin.site.register(Characteristic,CharacteristicAdmin)