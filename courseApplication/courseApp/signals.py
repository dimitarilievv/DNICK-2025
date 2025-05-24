import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from courseApp.models import Lecturer, Course

#Ако се избрише предавач, автоматски по случаен избор
# се распределуваат неговите курсеви на останатите достапни предавачи.
@receiver(pre_delete,sender=Lecturer)
def handle_delete(sender,instance,**kwargs):
    courses=Course.objects.filter(creator=instance.user)
    other_lecturers=Lecturer.objects.exclude(id=instance.id).all()

    for c in courses:
        new_lecturer=random.choice(other_lecturers)
        c.creator=new_lecturer.user
        c.save()

    course_lecturer_entries = instance.courses.all()

    for entry in course_lecturer_entries:
        new_lecturer = random.choice(other_lecturers)
        entry.lecturer = new_lecturer
        entry.save()