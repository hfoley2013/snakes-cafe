from textwrap import dedent

# Proof of life
# def hello_world():
#     print('Hello World!')

def intro_message():
    print(dedent("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """))

def appetizers_list():
    global apps
    apps = ["Wings", "Cookies", "Spring Rolls"]
    print(dedent("""
    Appetizers
    ----------"""))
    for app in apps:
        print(dedent(app))

def entrees_list():
    global entrees
    entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    print(dedent("""
    Entrees
    -------"""))
    for entree in entrees:
        print(dedent(entree))

def desserts_list():
    global desserts
    desserts = ["Ice Cream", "Cake", "Pie"]
    print(dedent("""
    Desserts
    --------"""))
    for dessert in desserts:
        print(dedent(dessert))

def drinks_list():
    global drinks
    drinks = ["Coffee", "Tea", "Unicorn Tears"]
    print(dedent("""
    Drinks
    ------"""))
    for drink in drinks:
        print(dedent(drink))

def show_menu():
    appetizers_list()
    entrees_list()
    desserts_list()
    drinks_list()

def data_validation():
    global menu_validation
    menu_validation = []
    full_menu = apps + entrees + desserts + drinks
    for item in full_menu:
        menu_validation.append(item.lower())



def take_order():
    data_validation()
    user_order = {}
    print(dedent("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """))
    ask_for_order = True
    while ask_for_order is True:
        order = input("> ")
        if menu_validation

intro_message()
show_menu()
take_order()