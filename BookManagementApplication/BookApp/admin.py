from django.contrib import admin

from BookApp.models import Book, Genre, Author, Rating


# Register your models here.

class BookRatingInline(admin.TabularInline):
    model = Rating
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","release_date","user","is_available")
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)
    def has_change_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_delete_permission(self, request, obj = None):
        if obj and obj.user == request.user:
            return True
        return False
    inlines = [BookRatingInline,]
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


class RatingAdmin(admin.ModelAdmin):
    list_display = ("book",)
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RatingAdmin, self).save_model(request, obj, form, change)
    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_add_permission(self, request, obj = None):
        return True
    exclude = ("user",)


admin.site.register(Book,BookAdmin)
admin.site.register(Genre,GenreAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Rating,RatingAdmin)