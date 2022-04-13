from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def view_menu(request):
    context = {'dish': dict()}
    for recipes in DATA:
        context['dish'].update({f'{recipes}': f'/{recipes}/'})
    return render(request, 'calculator/menu.html', context)


def view_recipe(request, dish):
    persons = int(request.GET.get('persons', '1'))
    recipe = dict()
    for ingredient, amount in DATA[dish].items():
        recipe[ingredient] = amount*persons
    context = {'dish': dish, 'recipe': recipe}
    return render(request, 'calculator/index.html', context)
