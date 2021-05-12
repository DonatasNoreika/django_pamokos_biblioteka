from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, BookReview


# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # išjungia placeholder'ius
    readonly_fields = ('id',)
    can_delete = False


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'reader', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    search_fields = ('id', 'book__title')
    list_editable = ('due_back', 'status')

    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'reader')
        }),
    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_books')


class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'date_created', 'reviewer', 'content')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(BookReview, BookReviewAdmin)
