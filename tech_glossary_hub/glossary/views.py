from django.shortcuts import render, get_object_or_404
from .models import Category, GlossaryTerm


def home(request):
    categories = Category.objects.all()

    latest_terms = (
        GlossaryTerm.objects.select_related("category")
        .order_by("-created_at")[:6]
    )

    context = {
        "categories": categories,
        "latest_terms": latest_terms,
        "total_categories": Category.objects.count(),
        "total_terms": GlossaryTerm.objects.count(),
        "difficulty_levels": 3,
    }

    return render(request, "glossary/home.html", context)



def about(request):
    return render(request, "glossary/about.html")



def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "glossary/category_list.html",
        {
            "categories": categories
        },
    )


def category_detail(request, slug):

    category = get_object_or_404(
        Category,
        slug=slug
    )

    terms = (
        GlossaryTerm.objects
        .filter(category=category)
        .order_by("title")
    )

    return render(
        request,
        "glossary/category_detail.html",
        {
            "category": category,
            "terms": terms,
        },
    )
    

def glossary_list(request):

    terms = (
        GlossaryTerm.objects
        .select_related("category")
        .order_by("title")
    )

    return render(
        request,
        "glossary/glossary_list.html",
        {
            "terms": terms
        }
    )


def glossary_detail(request, slug):

    term = get_object_or_404(
        GlossaryTerm.objects.select_related("category"),
        slug=slug
    )

    return render(
        request,
        "glossary/glossary_detail.html",
        {
            "term": term
        }
    )
    

