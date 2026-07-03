from django.contrib import admin
from .models import Category, GlossaryTerm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "created_at",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "name",
    )


@admin.register(GlossaryTerm)
class GlossaryTermAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "difficulty",
        "is_featured",
        "created_at",
    )

    list_filter = (
        "category",
        "difficulty",
        "is_featured",
    )

    search_fields = (
        "title",
        "definition",
        "explanation",
        "example",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    autocomplete_fields = (
        "category",
    )

    ordering = (
        "title",
    )