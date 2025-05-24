from django.db.models import Count
from django.contrib import admin, messages

from courseApp.models import *


# Register your models here.
class CourseLecturerInline(admin.TabularInline):
    model=CourseLecturer
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    exclude = ["creator",]
    inlines = [CourseLecturerInline,]
    def get_queryset(self, request):
        return Course.objects.filter(creator=request.user)
    def has_add_permission(self, request):
        lecturer = Lecturer.objects.filter(user=request.user).first()
        return bool(lecturer and lecturer.academic_title == "p")

    def save_model(self, request, obj, form, change):
        obj.creator=request.user
        #Курс со исто име не може да постои повеќе пати
        if Course.objects.filter(name=obj.name).exists():
            return
        return super(CourseAdmin,self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.creator==request.user
    def has_delete_permission(self, request, obj=None):
        return obj and obj.creator == request.user
    def has_view_permission(self, request, obj=None):
        return True


class LecturerAdmin(admin.ModelAdmin):
    exclude = ["user", ]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    def has_add_permission(self, request):
        return request.user.is_superuser
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        #Во admin панелот им се прикажуваат само предавачи што предаваат на помалку од 2 курсеви.
        qs=super(LecturerAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(courses_count=Count("courses")).filter(courses_count__lt=2)
        return qs

class CourseLecturerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Секој предавач може да учествува на најмногу 3 курса истовремено.
        if not change and obj.lecturer.courses.all().count()>=3:
            messages.warning(request, "This lecturer cant have more than 3 courses")
            return
        #Ако курсот има повеќе од 5 предавачи, се прикажува предупредување во админ панелот.
        if not change and obj.course.courselecturer_set.count() + 1 >= 5:
            messages.warning(request, "This course has more than 5")
            return

        #Вкупната должина (во денови) на курсевите што ги предава еден предавач не смее да надмине 365 дена.
        existing_courses = CourseLecturer.objects.select_related('course').filter(lecturer=obj.lecturer).exclude(course=obj.course)
        total_days = sum(
            (cl.course.date_end - cl.course.date_start).days
            for cl in existing_courses
            if cl.course.date_start and cl.course.date_end
        )
        new_course_duration = (obj.course.date_end - obj.course.date_start).days \
            if obj.course.date_start and obj.course.date_end else 0

        if total_days + new_course_duration > 365:
             messages.warning(request, f"Total days should not have 365 days. Now it is {total_days + new_course_duration}")
             return

        return super().save_model(request, obj, form, change)


admin.site.register(Course,CourseAdmin)
admin.site.register(Lecturer,LecturerAdmin)
admin.site.register(CourseLecturer,CourseLecturerAdmin)