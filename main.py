import random                                # For random suggestions
import sys
import os           # For clearing Terminal
from time import sleep      # Default time = 3 Seconds

try:    # Optional for style, importing pyfiglet module
    from pyfiglet import Figlet
    f = Figlet(font='big')
    print(f.renderText('Merryweather Cheesecake'))
except (ImportError, ModuleNotFoundError):
    pass

random_choice = ["Bread cheesecakes", "No egg cheesecakes", "Low amount cheese cheesecakes", 'Egg cheesecakes', 'Cappuccino']
cart = []

def cls():
    if sys.platform.startswith(('win32', 'win64', 'win86')):
        os.system('cls')
    else:
        os.system('clear')

def limit():
    cls()
    print('Sorry, you cannot order more than 10 items.')
    sleep(3)

def get_name(shop_name='Merryweather Cheesecakes'):
    name = input("Can I have your name, please?\n\n> ").strip()
    cls()
    if name and name.isalpha():
        print(f"Hello {name.title()}, welcome to {shop_name}.\n")
        order()
    else:
        print("Invalid input. Please enter a valid name.")
        get_name()

def unavailable():
    cls()
    suggestion = random.choice(random_choice)
    response = input(f"Sorry, the item is currently unavailable. Would you like to try our {suggestion}? (Yes/No)\n\n> ").strip().lower()
    
    if response in ['yes', 'y']:
        if suggestion == 'Bread cheesecakes':
            bread_cheesecake()
        elif suggestion == 'No egg cheesecakes':
            no_egg_cheesecake()
        elif suggestion == 'Low amount cheese cheesecakes':
            low_amount_cheese()
        elif suggestion == 'Egg cheesecakes':
            egg_cheesecake()
        elif suggestion == 'Cappuccino':
            cappuccino()
    elif response in ['no', 'n']:
        cls()
        print("Okay, some other time.\n")
        order()
    else:
        print("Please enter 'Yes' or 'No'.")
        unavailable()

def order():
    print("Here is our menu: \n\na) Bread cheesecake \nb) No egg cheesecake \nc) Low cheese cheesecake \nd) Egg cheesecake \ne) Cappuccino \nf) Random Suggestion")
    choice = input("Enter option (a-f) or '1' to exit: ").strip().lower()
    
    menu_options = {
        'a': bread_cheesecake,
        'b': no_egg_cheesecake,
        'c': low_amount_cheese,
        'd': egg_cheesecake,
        'e': cappuccino,
        'f': random_suggestion,
        '1': exit
    }
    
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid selection, please try again.")
        order()

def random_suggestion():
    cls()
    suggestion = random.choice(random_choice)
    response = input(f"We think you would like our {suggestion}. Would you like to try it? (Yes/No)\n\n> ").strip().lower()
    
    if response in ['yes', 'y']:
        unavailable()
    elif response in ['no', 'n']:
        cls()
        print("Okay, some other time.\n")
        order()
    else:
        print("Please enter 'Yes' or 'No'.")
        random_suggestion()

def bread_cheesecake():
    cls()
    print("Ordering Bread Cheesecake...")
    cart.append("Bread Cheesecake")
    order()

def no_egg_cheesecake():
    cls()
    print("Ordering No Egg Cheesecake...")
    cart.append("No Egg Cheesecake")
    order()

def low_amount_cheese():
    cls()
    print("Ordering Low Amount Cheese Cheesecake...")
    cart.append("Low Amount Cheese Cheesecake")
    order()

def egg_cheesecake():
    cls()
    print("Ordering Egg Cheesecake...")
    cart.append("Egg Cheesecake")
    order()

def cappuccino():
    cls()
    print("Ordering Cappuccino...")
    cart.append("Cappuccino")
    order()

# Start the chatbot
get_name()
