# from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe

# from utils.recipes.factory import make_recipe


def home(request):
    all_recipes = Recipe.objects.filter(is_pablish=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={"recipes": all_recipes},
    )


def category(request, category_id):
    all_recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id, is_pablish=True
        ).order_by(  # noqa E501
            "-id"
        ),
    )

    # if not all_recipes:
    #     raise Http404("Page Not Found")

    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": all_recipes,
            "title": f"{all_recipes[0].category.nome} - Categoria |",
        },
    )


def recipes(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id, is_pablish=True)
    return render(
        request,
        "recipes/pages/recipe.html",
        context={
            "recipe": recipe,
            "is_detail_page": True,
        },
    )
