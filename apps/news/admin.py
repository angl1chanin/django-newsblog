from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from news.models import Article, Category, Tag
from news.forms import ArticleAdminForm


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    fields = ('author', 'title', 'photo', 'get_photo', 'content', 'category', 'tags', 'upvotes', 'downvotes', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'upvotes', 'downvotes', 'created_at', 'updated_at', 'get_photo')
    search_fields = ('title', 'content')
    form = ArticleAdminForm
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{ obj.photo.url }' alt='photo' width='300'>")

    get_photo.short_description = 'Миниатюра'

    # def save_model(self, request, obj, form, change):
    #     """When creating a new object, set the creator field.
    #     """
    #     if not obj.author:
    #         obj.author = request.user
    #     obj.save()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'photo', 'get_photo', 'slug')
    list_display = ('id', 'title')
    readonly_fields = ('get_photo', 'slug')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{ obj.photo.url }' alt='photo' width='300'>")

    get_photo.short_description = 'Миниатюра'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
