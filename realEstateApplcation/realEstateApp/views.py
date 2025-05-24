from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect

from realEstateApp.forms import RealEstateForm
from realEstateApp.models import RealEstate, RealEstateCharacteristic, Characteristic


# Create your views here.
#Недвижноста нема почетна цена, туку таа се креира како сума од вредностите на карактеристиките
#кои таа недвижност ги поседува. На пример, доколку недвижнота располага со лифт, тогаш во
# цената се додава $10000, поседувањето на базен е $25000 итн
def index(request):
    real_estates=RealEstate.objects.filter(area__gt=100,is_sold=False).all()
    dict=[]
    for re in real_estates:
        price=0
        real_estate_characteristic=RealEstateCharacteristic.objects.filter(real_estate=re)
        for rec in real_estate_characteristic:
            price += rec.characteristic.price
        dict.append({'re':re,'price': price})

    context={'re': dict}
    return render(request,'index.html',context)

# карактеристиките на една недвижност се одделени со запирка. Доколку се додадат
# нови карактеристики или некои од постоечките се отстранат, цената треба автоматски да се ажурира
def edit(request,id=None):
    real_estate=get_object_or_404(RealEstate,pk=id)

    if request.method=='POST':
        form=RealEstateForm(request.POST,request.FILES,instance=real_estate)
        if form.is_valid:
            real_estate=form.save()
            real_estate.save()

            characteristics_raw=form.cleaned_data['characteristics']
            characteristics_names=[name.strip() for name in characteristics_raw.split(',') if name.strip()]

            for name in characteristics_names:
                characteristic, created=Characteristic.objects.get_or_create(name=name)
                RealEstateCharacteristic.objects.create(real_estate=real_estate,characteristic=characteristic)
            form.save()
        return redirect('index')
    else:
        # Претходно дефинирани карактеристики за прикажување во формата
        existing_chars = RealEstateCharacteristic.objects.filter(real_estate=real_estate).values_list(
            'characteristic__name', flat=True)
        chars_string = ', '.join(existing_chars)
        form = RealEstateForm(instance=real_estate, initial={'characteristics': chars_string})
    # form=RealEstateForm(instance=real_estate)
    return render(request,"edit.html",context={"form":form,'id':id,'real_estate':real_estate})

