from django.shortcuts import render
from .models import Category, GlossaryTerm


def home(request):
    categories = Category.objects.all()

    latest_terms = GlossaryTerm.objects.select_related("category").order_by("-created_at")[:6]

    featured_terms = GlossaryTerm.objects.filter(is_featured=True)[:6]

    context = {
        "categories": categories,
        "latest_terms": latest_terms,
        "featured_terms": featured_terms,
        "total_categories": Category.objects.count(),
        "total_terms": GlossaryTerm.objects.count(),
        "difficulty_levels": 3,
    }

    return render(request, "glossary/home.html", context)