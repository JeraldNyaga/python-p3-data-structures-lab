spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [spicyfood["name"] for spicyfood in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [spicyfood for spicyfood in spicy_foods if spicyfood["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for spicyfood in spicy_foods:
        print(f'{spicyfood["name"]} ({spicyfood["cuisine"]}) | Heat Level: {"🌶" * spicyfood["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for cuisine_meal in spicy_foods:
        if cuisine_meal["cuisine"] == cuisine:
            return cuisine_meal

def print_spiciest_foods(spicy_foods):
    for spicyfood in spicy_foods:
        if spicyfood["heat_level"] > 5:
            print(f'{spicyfood["name"]} ({spicyfood["cuisine"]}) | Heat Level: {"🌶" * spicyfood["heat_level"]}')

def get_average_heat_level(spicy_foods):
    foods = 0
    heat_level = 0
    for spicyfood in spicy_foods:
        foods +=1
        heat_level += spicyfood["heat_level"]
    return heat_level / foods

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

