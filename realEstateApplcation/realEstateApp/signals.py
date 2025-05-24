from django.db.models.signals import pre_save
from django.dispatch import receiver

from realEstateApp.models import RealEstate, RealEstateAgent


#Кога еден оглас/недвижнина ќе се означи како продадена,
#потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба

@receiver(pre_save,sender=RealEstate)
def handle_sold(sender,instance,**kwargs):
    old_instance=sender.objects.filter(id=instance.id).first()
    if old_instance:
        if old_instance.is_sold != instance.is_sold:
            realestate_agents=RealEstateAgent.objects.filter(real_estate=old_instance).all()
            for re in realestate_agents:
                agent=re.agent
                agent.number_sales+=1
                agent.save()