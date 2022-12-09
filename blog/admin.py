from django.contrib import admin
from django import forms

from .models import Post, Comment
from modeltranslation.admin import TranslationAdmin

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content_uz = forms.CharField(label="Matn",widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Description",widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(label="Описание",widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'




class PostAdmin(TranslationAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ( "title", "slug", "status", "created_on")
    list_filter = ( "status", "created_on")
    search_fields = ["title", "content"]
    form=PostAdminForm

class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)