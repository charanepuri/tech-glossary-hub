from rest_framework import serializers
from .models import Category, GlossaryTerm


class CategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = Category

        fields = "__all__"
        
class GlossarySerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()

    class Meta:

        model = GlossaryTerm

        fields = [

            "id",

            "title",

            "slug",

            "definition",

            "explanation",

            "example",

            "difficulty",

            "is_featured",

            "created_at",

            "category",

        ]

