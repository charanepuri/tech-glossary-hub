from django.db.models import Q
from rest_framework import generics

from .models import Category, GlossaryTerm
from .serializers import CategorySerializer, GlossarySerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GlossaryListAPIView(generics.ListAPIView):
    queryset = GlossaryTerm.objects.select_related("category").all()
    serializer_class = GlossarySerializer


class GlossaryDetailAPIView(generics.RetrieveAPIView):
    queryset = GlossaryTerm.objects.select_related("category")
    serializer_class = GlossarySerializer
    lookup_field = "slug"


class GlossarySearchAPIView(generics.ListAPIView):
    serializer_class = GlossarySerializer

    def get_queryset(self):
        query = self.request.GET.get("q")

        queryset = GlossaryTerm.objects.select_related("category")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(definition__icontains=query)
                | Q(explanation__icontains=query)
            )

        return queryset


class GlossaryFilterAPIView(generics.ListAPIView):
    serializer_class = GlossarySerializer

    def get_queryset(self):
        queryset = GlossaryTerm.objects.select_related("category")

        category = self.request.GET.get("category")
        difficulty = self.request.GET.get("difficulty")

        if category:
            queryset = queryset.filter(category__slug=category)

        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        return queryset