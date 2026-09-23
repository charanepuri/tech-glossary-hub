from django.shortcuts import render, get_object_or_404
from .models import Category, GlossaryTerm
from django.db.models import Q
from django.core.paginator import Paginator

# ==========================================================
# CUSTOM ERROR HANDLERS
# ==========================================================

handler404 = "glossary.views.custom_404"
handler500 = "glossary.views.custom_500"

def home(request):

     
    categories = Category.objects.prefetch_related("terms")


    # latest_terms = (
    #     GlossaryTerm.objects
    #     .select_related("category")
    #     .order_by("-created_at")[:6]
    # )
    
    latest_terms = (

    GlossaryTerm.objects

    .select_related("category")

    .order_by("-created_at")[:6]

)

    # featured_terms = (
    #     GlossaryTerm.objects
    #     .select_related("category")
    #     .filter(is_featured=True)[:6]
    # )
    featured_terms = (

    GlossaryTerm.objects

    .select_related("category")

    .filter(is_featured=True)[:6]

)

    context = {

        "categories": categories,

        "latest_terms": latest_terms,

        "featured_terms": featured_terms,

        "total_categories": categories.count(),

        "total_terms": GlossaryTerm.objects.count(),

        "featured_count": GlossaryTerm.objects.filter(
            is_featured=True
        ).count(),

        "beginner_count": GlossaryTerm.objects.filter(
            difficulty="Beginner"
        ).count(),

        "intermediate_count": GlossaryTerm.objects.filter(
            difficulty="Intermediate"
        ).count(),

        "advanced_count": GlossaryTerm.objects.filter(
            difficulty="Advanced"
        ).count(),

    }

    return render(
        request,
        "glossary/home.html",
        context
    )


def about(request):
    return render(request, "glossary/about.html")


def versions(request):
    return render(request, "glossary/versions.html")


def contact(request):
    return render(request, "glossary/contact.html")



def category_list(request):
    # categories = Category.objects.all()
    categories = (
    Category.objects
    .prefetch_related("terms")
)

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
        .select_related("category")
        .filter(category=category)
    )

    context = {
        "category": category,
        "terms": terms,
    }

    return render(
        request,
        "glossary/category_detail.html",
        context
    )
    

def glossary_list(request):

    terms_list = (
        GlossaryTerm.objects
        .select_related("category")
        .order_by("title")
    )

    paginator = Paginator(terms_list, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "glossary/glossary_list.html",
        {
            "terms": page_obj,
            "total_count": terms_list.count(),
        }
    )


def glossary_detail(request, slug):

    term = get_object_or_404(
        GlossaryTerm.objects.select_related("category"),
        slug=slug
    )

    related_terms = (
        GlossaryTerm.objects.select_related("category")
        .filter(category=term.category)
        .exclude(id=term.id)[:4]
    )

    featured_terms = (
        GlossaryTerm.objects
        .select_related("category")
        .filter(is_featured=True)
        .exclude(id=term.id)[:6]
    )

    previous_term = (
        GlossaryTerm.objects
        .filter(id__lt=term.id)
        .order_by("-id")
        .first()
    )

    next_term = (
        GlossaryTerm.objects
        .filter(id__gt=term.id)
        .order_by("id")
        .first()
    )

    context = {
        "term": term,
        "related_terms": related_terms,
        "featured_terms": featured_terms,
        "previous_term": previous_term,
        "next_term": next_term,
    }

    return render(
        request,
        "glossary/glossary_detail.html",
        context
    )


def search_terms(request):

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "")
    difficulty = request.GET.get("difficulty", "")
    sort = request.GET.get("sort", "")

    terms = GlossaryTerm.objects.select_related("category").all()

    # Search
    if query:
        terms = terms.filter(
            Q(title__icontains=query) |
            Q(definition__icontains=query) |
            Q(explanation__icontains=query)
        )

    # Category Filter
    if category:
        terms = terms.filter(category__slug=category)

    # Difficulty Filter
    if difficulty:
        terms = terms.filter(difficulty=difficulty)

    # Sorting
    if sort == "az":
        terms = terms.order_by("title")

    elif sort == "za":
        terms = terms.order_by("-title")

    elif sort == "oldest":
        terms = terms.order_by("created_at")

    else:
        terms = terms.order_by("-created_at")

    paginator = Paginator(terms, 9)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "query": query,
        "page_obj": page_obj,
        "result_count": terms.count(),
        "categories": Category.objects.all(),
        "selected_category": category,
        "selected_difficulty": difficulty,
        "selected_sort": sort,
    }

    return render(
        request,
        "glossary/search_results.html",
        context
    )



def custom_404(request, exception):
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


