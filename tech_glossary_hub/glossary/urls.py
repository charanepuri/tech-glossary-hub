from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),
    
    path(
        "about/",
        views.about,
        name="about"
    ),

    path(
        "categories/",
        views.category_list,
        name="category_list"
    ),

    path(
        "categories/<slug:slug>/",
        views.category_detail,
        name="category_detail"
    ),
    
    path(
        "glossary/",
        views.glossary_list,
        name="glossary_list"
    ),
    
    path(
        "glossary/<slug:slug>/",
        views.glossary_detail,
        name="glossary_detail"
    ),
    
    
    
    path("search/", views.search_terms, name="search_terms"),

]



# ==========================================================
# CUSTOM ERROR HANDLERS
# ==========================================================

handler404 = "glossary.views.custom_404"
handler500 = "glossary.views.custom_500"