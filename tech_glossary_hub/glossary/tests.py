from django.test import TestCase, Client
from django.urls import reverse
from .models import Category, GlossaryTerm, DifficultyChoices


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Cloud Computing",
            description="Concepts related to cloud technologies.",
            icon="bi-cloud",
            color="#0ea5e9"
        )

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Cloud Computing")

    def test_category_slug_auto_generation(self):
        self.assertEqual(self.category.slug, "cloud-computing")


class GlossaryTermModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Programming",
            description="General programming concepts.",
        )
        self.term = GlossaryTerm.objects.create(
            category=self.category,
            title="Polymorphism",
            definition="The ability of different objects to respond to the same message.",
            explanation="Detailed explanation of polymorphism.",
            example="class Dog: speak() ... class Cat: speak() ...",
            difficulty=DifficultyChoices.INTERMEDIATE,
            is_featured=True
        )

    def test_glossary_term_string_representation(self):
        self.assertEqual(str(self.term), "Polymorphism")

    def test_glossary_term_slug_auto_generation(self):
        self.assertEqual(self.term.slug, "polymorphism")


class PageViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Python",
            description="Python programming language concepts.",
            icon="bi-filetype-py",
            color="#ffc107"
        )
        self.term1 = GlossaryTerm.objects.create(
            category=self.category,
            title="Decorators",
            definition="A decorator modifies a function without changing its source code.",
            explanation="Decorators wrap another function.",
            example="@my_decorator\ndef func(): pass",
            difficulty=DifficultyChoices.INTERMEDIATE,
            is_featured=True
        )
        self.term2 = GlossaryTerm.objects.create(
            category=self.category,
            title="Generators",
            definition="Functions that yield values one at a time.",
            explanation="Generators use yield keyword.",
            example="def gen(): yield 1",
            difficulty=DifficultyChoices.ADVANCED,
            is_featured=False
        )

    def test_home_page_status_and_content(self):
        response = self.client.get(reverse("home"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tech Glossary Hub")
        self.assertContains(response, "Python")

    def test_about_page_status(self):
        response = self.client.get(reverse("about"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "About Tech Glossary Hub")

    def test_versions_page_status_and_content(self):
        response = self.client.get(reverse("versions"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Versions")
        self.assertContains(response, "Django Version")
        self.assertContains(response, "HTML Version")
        self.assertContains(response, "React Version")
        self.assertContains(response, "Angular Version")
        self.assertContains(response, "Flask Version")
        self.assertContains(response, "Full Stack Version")

    def test_contact_page_status_and_content(self):
        response = self.client.get(reverse("contact"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Get in Touch")
        self.assertContains(response, "PP_IMG.png")
        self.assertContains(response, "LinkedIn")
        self.assertContains(response, "GitHub")
        self.assertContains(response, "portfolio-site-django.onrender.com")

    def test_category_list_page(self):
        response = self.client.get(reverse("category_list"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python")

    def test_category_detail_page(self):
        response = self.client.get(reverse("category_detail", kwargs={"slug": self.category.slug}), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Decorators")
        self.assertContains(response, "Generators")

    def test_glossary_detail_page_and_exclusion(self):
        response = self.client.get(reverse("glossary_detail", kwargs={"slug": self.term1.slug}), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Decorators")
        # Ensure the current term is excluded from the featured recommendations context
        featured_terms = response.context["featured_terms"]
        self.assertNotIn(self.term1, featured_terms)

    def test_custom_404_page(self):
        response = self.client.get("/non-existent-endpoint-xyz/", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "404", status_code=404)
        self.assertContains(response, "Page Not Found", status_code=404)


class PaginationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Django", description="Django framework")
        # Create 15 terms to test pagination (page size = 9)
        for i in range(15):
            GlossaryTerm.objects.create(
                category=self.category,
                title=f"Term {i:02d}",
                definition=f"Definition {i}",
                explanation=f"Explanation {i}",
                example=f"Example {i}"
            )

    def test_glossary_list_first_page(self):
        response = self.client.get(reverse("glossary_list"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["terms"].has_other_pages())
        self.assertEqual(len(response.context["terms"]), 9)
        self.assertEqual(response.context["total_count"], 15)

    def test_glossary_list_second_page(self):
        response = self.client.get(reverse("glossary_list") + "?page=2", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["terms"]), 6)

    def test_glossary_list_invalid_page_handles_gracefully(self):
        # Out-of-bounds page delivers the last page
        response = self.client.get(reverse("glossary_list") + "?page=999", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["terms"].number, 2)

        # Non-integer page delivers the first page
        response_non_int = self.client.get(reverse("glossary_list") + "?page=invalid", HTTP_HOST="127.0.0.1")
        self.assertEqual(response_non_int.status_code, 200)
        self.assertEqual(response_non_int.context["terms"].number, 1)


class SearchAndFilterTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cat_python = Category.objects.create(name="Python", description="Python lang")
        self.cat_js = Category.objects.create(name="JavaScript", description="JS lang")

        self.term1 = GlossaryTerm.objects.create(
            category=self.cat_python,
            title="List Comprehension",
            definition="Concise way to create lists.",
            explanation="[x for x in iterable]",
            example="[i for i in range(10)]",
            difficulty=DifficultyChoices.BEGINNER
        )
        self.term2 = GlossaryTerm.objects.create(
            category=self.cat_js,
            title="Async Await",
            definition="Syntactic sugar for Promises in JS.",
            explanation="Simplifies asynchronous code.",
            example="async function test() { await fetch(); }",
            difficulty=DifficultyChoices.INTERMEDIATE
        )

    def test_search_by_query(self):
        response = self.client.get(reverse("search_terms") + "?q=Comprehension", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "List Comprehension")
        self.assertNotContains(response, "Async Await")

    def test_filter_by_category(self):
        response = self.client.get(reverse("search_terms") + f"?category={self.cat_python.slug}", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "List Comprehension")
        self.assertNotContains(response, "Async Await")

    def test_filter_by_difficulty(self):
        response = self.client.get(reverse("search_terms") + "?difficulty=Intermediate", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Async Await")
        self.assertNotContains(response, "List Comprehension")


class APITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name="Database",
            description="Database concepts and management."
        )
        self.term = GlossaryTerm.objects.create(
            category=self.category,
            title="SQL",
            definition="Structured Query Language for managing relational databases.",
            explanation="Used for CRUD operations.",
            example="SELECT * FROM users;",
            difficulty=DifficultyChoices.BEGINNER,
            is_featured=True
        )

    def test_categories_api(self):
        response = self.client.get(reverse("api_categories"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        results = data.get("results", data)
        self.assertTrue(any(c["name"] == "Database" for c in results))

    def test_glossary_list_api(self):
        response = self.client.get(reverse("api_glossary"), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        results = data.get("results", data)
        self.assertTrue(any(t["title"] == "SQL" for t in results))

    def test_glossary_detail_api(self):
        response = self.client.get(reverse("api_glossary_detail", kwargs={"slug": self.term.slug}), HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "SQL")

    def test_glossary_search_api(self):
        response = self.client.get(reverse("api_search") + "?q=Structured", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        results = data.get("results", data)
        self.assertTrue(any(t["title"] == "SQL" for t in results))

    def test_glossary_filter_api(self):
        response = self.client.get(reverse("api_filter") + f"?category={self.category.slug}&difficulty=Beginner", HTTP_HOST="127.0.0.1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        results = data.get("results", data)
        self.assertTrue(any(t["title"] == "SQL" for t in results))
