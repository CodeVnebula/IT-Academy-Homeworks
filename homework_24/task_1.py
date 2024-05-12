import json
from time import sleep
from os import system

def load_json(file_path: str):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        
            return data
    except FileNotFoundError:
        print("File does not exist Or could not be opened!")
        return None

def which_meal_to_cook(recipes: dict) -> list:
    meals = {}
    ingredients_for_meal = []
    print("Which meal do you want to cook?")
    for i, key in enumerate(recipes.keys()):
        meals[i+1] = key
        print(f"{i+1} - {key}")
    
    while True:
        choice = int(input(">> "))
        if choice <= i+1 and choice > 0:
            break
        else:
            print("Please enter approapriate number of choice!")
    
    sleep(2)
    system("cls")
    print(f"Ingredients needed for {meals[choice]}:")
    sleep(1)
    for ingredient in recipes[meals[choice]]["ingredients"]:
        sleep(0.3)
        ingredients_for_meal.append(ingredient)
        print(f"  - {ingredient}")
    
    print()
    return ingredients_for_meal

def where_to_buy_ingredients(markets: dict, ingredients: list):
    markets_to_aim = {}
    route = []
    
    print("Finding best route for you in local city markets...")
    sleep(2)
    
    while ingredients: 
        for key, value in markets.items():
            common = len(set(value).intersection(ingredients))
            markets_to_aim[key] = common
        
        max_common = max(markets_to_aim.values())
        
        # If the maximum common ingredients found is 0, it means none of the markets have the ingredients
        if max_common == 0:
            print("You can't buy ingredients for this product in this city")
            return  # Exiting the function as there's no point in continuing
        
        for key, value in markets_to_aim.items():
            if value == max_common:
                market = key
                route.append(market)
                break
        
        print(f"Go to {market} for:")
        
        for ingredient in ingredients[:]: 
            if ingredient in markets[market]:
                sleep(0.2)
                print(f"  - {ingredient}")
                ingredients.remove(ingredient)


def main():
    MARKETS_PATH = "homework_24/resources/markets.json"
    RECIPES_PATH = "homework_24/resources/recipes.json"
    
    recipes = load_json(RECIPES_PATH)
    markets = load_json(MARKETS_PATH)
    
    ingredients = which_meal_to_cook(recipes)
    where_to_buy_ingredients(markets=markets, ingredients=ingredients)
    
    
if __name__ == "__main__":
    main()
