from django.shortcuts import redirect, render

from .models import FoodItem


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            FoodItem.objects.create(name=name, calories=calories)
        return redirect('home')

    foods = FoodItem.objects.order_by('-created_at')
    total_calories = sum(food.calories for food in foods)
    return render(request, 'caloriecounter/home.html', {
        'foods': foods,
        'total_calories': total_calories,
    })


def delete_food(request, food_id):
    FoodItem.objects.filter(id=food_id).delete()
    return redirect('home')


def reset_foods(request):
    FoodItem.objects.all().delete()
    return redirect('home')
