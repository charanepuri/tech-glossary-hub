from django.urls import path

from . import api_views

urlpatterns = [

    path(

        "categories/",

        api_views.CategoryListAPIView.as_view(),

        name="api_categories",

    ),

    path(

        "glossary/",

        api_views.GlossaryListAPIView.as_view(),

        name="api_glossary",

    ),

    path(

        "glossary/<slug:slug>/",

        api_views.GlossaryDetailAPIView.as_view(),

        name="api_glossary_detail",

    ),

    path(

        "search/",

        api_views.GlossarySearchAPIView.as_view(),

        name="api_search",

    ),

    path(

        "filter/",

        api_views.GlossaryFilterAPIView.as_view(),

        name="api_filter",

    ),

]