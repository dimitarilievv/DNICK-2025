from django.contrib import admin

from BookApp.models import Book, Genre, Author, Rating, BookTranslator, Translator

# Register your models here.

class BookRatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    # exclude = ("user",)
    readonly_fields = ("user",)

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return True
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)

        class CustomFormSet(formset):
            def save_new(self, form, commit=True):
                instance = super().save_new(form, commit=False)
                instance.user = request.user
                if commit:
                    instance.save()
                return instance

        return CustomFormSet

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","release_date","user","is_available")
    inlines = [BookRatingInline,]
    exclude = ("user",)
    list_filter = ("is_available",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)
    def has_change_permission(self, request, obj = None):
        return True
    def has_delete_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False
    def get_readonly_fields(self, request, obj=None):
        if obj and obj.user != request.user:
            # ако книгата не е негова, сите полиња readonly
            return [f.name for f in self.model._meta.fields]
        return super().get_readonly_fields(request, obj)


class RatingAdmin(admin.ModelAdmin):
    list_display = ("book",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RatingAdmin, self).save_model(request, obj, form, change)
    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_add_permission(self, request, obj = None):
        return True
    exclude = ("user",)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","nationality")

class TranslatorAdmin(admin.ModelAdmin):
    list_display = ("name","nationality","date_of_birth")
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

class BookTranslatorAdmin(admin.ModelAdmin):
    list_display = ("book","translator",)
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Book,BookAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Translator,TranslatorAdmin)
admin.site.register(BookTranslator,BookTranslatorAdmin)