from django.contrib import admin
from django.db.models import Count

from cakeApp.models import Baker, Cake


# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    # exclude = ["baker",]
    # Тортите можат да бидат менувани само од пекарите кои ги додале
    # останатите пекари може само да ги гледаат тие торти.
    def has_change_permission(self, request, obj=None):
        return obj and obj.baker.user == request.user
    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        #Го наоѓаш првиот Baker кој припаѓа на тековниот пријавен корисник.
        baker=Baker.objects.filter(user=request.user).first()
        baker_cakes=Cake.objects.filter(baker=baker).all()

        #Барање: Еден пекар може да има максимум 10 торти во дадено време.
        if not change and baker_cakes.count() == 10:
            return

        #Барање: Вкупната цена на тортите на еден пекар не смее да надминува 10 000.
        sum=0
        for cake in baker_cakes:
            sum += cake.price

        #Не можеш да додадеш нова торта ако со додавањето се надминува лимитот од 10,000 во цена.
        if not change and sum+obj.price > 10000:
            return

        #Ако има промена (change е True), значи менуваш постоечка торта.
        # се пресметува разликата помеѓу старата и новата цена
        old_cake_obj=baker_cakes.filter(id=obj.id).first()
        if change and sum+obj.price-old_cake_obj.price > 10000:
            return

        #Пекар не може да додаде торта, ако веќе постои торта со истото име.
        if Cake.objects.filter(name=obj.name).exists():
            return

        super(CakeAdmin, self).save_model(request, obj, form, change)

class BakerAdmin(admin.ModelAdmin):
    # exclude = ["user",]
    #Пекарите можат да бидат додадени, менувани и бришени само од супер-корисници.
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    #На супер-корисниците во Админ панелот им се прикажуваат пекарите со помалку од 5 торти.
    #get_queryset се користи во Django Admin за да се дефинира кои објекти ќе ги гледа корисникот во admin интерфејсот.
    def get_queryset(self, request):
        qs = super(BakerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(cakes_count=Count('cakes')).filter(cakes_count__lt=5)
        return qs


admin.site.register(Cake,CakeAdmin)
admin.site.register(Baker,BakerAdmin)
