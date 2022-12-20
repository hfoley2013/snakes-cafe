from textwrap import dedent

# Proof of life
# def hello_world():
#     print('Hello World!')

def intro_message():
    """
    Prints an intro headline to the users on the menu
    """
    print(dedent("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """))

def appetizers_list():
    """
    Generates a list of appetizers and prints them to the menu.
    The menu can be updated by adding items to the apps list.
    """
    global apps
    apps = ["Wings", "Cookies", "Spring Rolls"]
    print(dedent("""
    Appetizers
    ----------"""))
    for app in apps:
        print(dedent(app))

def entrees_list():
    """
    Generates a list of entrees and prints them to the menu.
    The menu can be updated by adding items to the entrees list.
    """
    global entrees
    entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    print(dedent("""
    Entrees
    -------"""))
    for entree in entrees:
        print(dedent(entree))

def desserts_list():
    """
    Generates a list of desserts and prints them to the menu.
    The menu can be updated by adding items to the desserts list.
    """
    global desserts
    desserts = ["Ice Cream", "Cake", "Pie"]
    print(dedent("""
    Desserts
    --------"""))
    for dessert in desserts:
        print(dedent(dessert))

def drinks_list():
    """
    Generates a list of drinks and prints them to the menu.
    The menu can be updated by adding items to the drinks list.
    """
    global drinks
    drinks = ["Coffee", "Tea", "Unicorn Tears"]
    print(dedent("""
    Drinks
    ------"""))
    for drink in drinks:
        print(dedent(drink))

def show_menu():
    """
    Calls the appetizers, entrees, desserts, and drinks functions to render the menu.
    """
    appetizers_list()
    entrees_list()
    desserts_list()
    drinks_list()

def data_validation():
    """
    Creates a full menu for data validation purposes.
    If the item ordered by the user is not inside the menu_validation list, the order will be rejected.
    """
    global menu_validation
    menu_validation = []
    full_menu = apps + entrees + desserts + drinks
    for item in full_menu:
        menu_validation.append(item.lower())



def take_order():
    """
    Prompts the user for their order.
    Compares their order to the full menu and allows the item to be added to the user_order if the item is on the menu.
    If the item is not on the menu, the user is asked to select another item.
    The user will be prompted for their order until they enter 'quit'.
    """
    data_validation()
    global user_order
    user_order = []
    print(dedent("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """))
    ask_for_order = True
    while ask_for_order:
        order = input(dedent("> ")).lower()
        if order == "quit":
            ask_for_order = False
            break
        if order in menu_validation:
            user_order.append(order)
            num_order = user_order.count(order)
            print(dedent(f"** {num_order} orders of {order} have been added to your meal **" if num_order > 1 else f"** {num_order} order of {order} have been added to your meal **"))
        else:
            print(dedent("That item is not on the menu. Please select another item."))

intro_message()
show_menu()
take_order()