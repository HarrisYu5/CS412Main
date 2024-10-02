from django.shortcuts import render
import random

# Create your views here.

def main(request):
    return render(request, 'main.html')

def order(request):
    dailySpecial = ["Golden Apple", "Potion of Health", "Fermented spider eye", "Mushroom stew", 
                    "Bread", "Cooked porkchop", "Cooked chicken", "Cooked salmon", "Cookie", "Cake"]
    dailySpecialPrice = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    randomIndex = random.randint(0, len(dailySpecial) - 1)
    special = dailySpecial[randomIndex]
    specialPrice = dailySpecialPrice[randomIndex]



    menu = {("Spicy Chicken", 10), 
            ("Loaded Poutine", 15), 
            ("Fries", 5), 
            ("Soda", 3),
            (special, specialPrice)}
    
    menuContext = {
        "menu": menu
    }
    return render(request, 'order.html', menuContext)

    
def confirmation(request):
    return render(request, 'confirmation.html')