
from lib.data_structures import *

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

def test_get_names():
    assert get_names(spicy_foods) == ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

def test_get_spiciest_foods():
    assert get_spiciest_foods(spicy_foods) == [
        {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
        {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
    ]

def test_print_spicy_foods(capsys):
    print_spicy_foods(spicy_foods)
    captured = capsys.readouterr()
    assert captured.out == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\nBuffalo Wings (American) | Heat Level: 🌶🌶🌶\nMapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

def test_get_spicy_food_by_cuisine():
    assert get_spicy_food_by_cuisine(spicy_foods, "American") == {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    }

def test_print_spiciest_foods(capsys):
    print_spiciest_foods(spicy_foods)
    captured = capsys.readouterr()
    assert captured.out == "Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶\nMapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶\n"

def test_average_heat_level():
    assert average_heat_level(spicy_foods) == 6

def test_create_spicy_food():
    new_food = {"name": "Griot", "cuisine": "Haitian", "heat_level": 10}
    updated_spicy_foods = create_spicy_food(spicy_foods, new_food)
    assert updated_spicy_foods[-1] == new_food
