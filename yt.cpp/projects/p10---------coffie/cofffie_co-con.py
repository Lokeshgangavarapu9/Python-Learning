import random
import coffie_logo

print(coffie_logo.logo)

# --- DATA CONFIGURATIONS ---
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18, "milk": 0},
        "price": 100,
    },
    "latte": {
        "ingredients": {"water": 200, "coffee": 24, "milk": 150},
        "price": 150,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "coffee": 24, "milk": 100},
        "price": 200,
    }
}

RAW_MATERIAL_COSTS = {
    "water": 0.1,  
    "milk": 0.3,   
    "coffee": 2.0  
}

OWNER_PASSWORD = "admin"
resources = {"water": 500, "milk": 500, "coffee": 100}
total_revenue_collected = 0.0  
total_raw_material_expense = 0.0

def calculate_inventory_expense(res_dict):
    return (res_dict["water"] * RAW_MATERIAL_COSTS["water"] +
            res_dict["milk"] * RAW_MATERIAL_COSTS["milk"] +
            res_dict["coffee"] * RAW_MATERIAL_COSTS["coffee"])

total_raw_material_expense += calculate_inventory_expense(resources)

# --- NEW FUNCTION: MENU DISPLAY ---
def display_menu():
    """Prints a beautiful price board of available items."""
    print("\n==============================")
    print("      ☕ COFFEE MENU ☕       ")
    print("==============================")
    for item, details in MENU.items():
        # Capitalizes item name and formats the price nicely
        print(f" Dispensing: {item.capitalize()} | Price: Rs. {details['price']}")
    print("==============================\n")

# --- CORE GAME FUNCTIONS ---

def print_report():
    print("\n========= MACHINE FINANCIAL & RESOURCE REPORT =========")
    print(f"Water  : {resources['water']}ml")
    print(f"Milk   : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Total Revenue Collected : Rs. {total_revenue_collected:.2f}")
    print(f"Total Material Expenses : Rs. {total_raw_material_expense:.2f}")
    
    net_profit_loss = total_revenue_collected - total_raw_material_expense
    if net_profit_loss >= 0:
        print(f"Current Financial State : 📈 PROFIT of Rs. {net_profit_loss:.2f}")
    else:
        print(f"Current Financial State : 📉 LOSS of Rs. {abs(net_profit_loss):.2f}")
    print("=======================================================\n")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("\nPlease insert coins.")
    print("⚠️ Machine only accepts ₹5, ₹10, and ₹20 coins.")
    try:
        fives = int(input("How many ₹5 coins?: ") or 0) * 5
        tens = int(input("How many ₹10 coins?: ") or 0) * 10
        twenties = int(input("How many ₹20 coins?: ") or 0) * 20
        return fives + tens + twenties
    except ValueError:
        print("Invalid entry. Non-numeric input registered as ₹0.")
        return 0

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

def refill_resources():
    global total_raw_material_expense
    print("\n--- REFILL RAW MATERIALS ---")
    try:
        new_water = int(input("Enter amount of Water to add (ml): ") or 0)
        new_milk = int(input("Enter amount of Milk to add (ml): ") or 0)
        new_coffee = int(input("Enter amount of Coffee to add (g): ") or 0)
        
        refill_batch = {"water": new_water, "milk": new_milk, "coffee": new_coffee}
        added_expense = calculate_inventory_expense(refill_batch)
        total_raw_material_expense += added_expense
        
        resources["water"] += new_water
        resources["milk"] += new_milk
        resources["coffee"] += new_coffee
        
        print(f"✅ Refill successful! Added Expenses: Rs. {added_expense:.2f}")
    except ValueError:
        print("Invalid values entered. Refill aborted.")


# --- MAIN MACHINE LOOP ---

machine_on = True

while machine_on:
    # 1. First, show the available items board
    display_menu()
    
    # 2. Next, show the selection menu prompt
    choice = input("What would you like to have? (latte / espresso / cappuccino):\n👉 Choice: ").lower().strip()
    
    match choice:
        case "espresso" | "latte" | "cappuccino":
            drink = MENU[choice]
            
            if is_resource_sufficient(drink["ingredients"]):
                inserted_money = process_coins()
                drink_cost = drink["price"]
                
                if inserted_money >= drink_cost:
                    total_revenue_collected += drink_cost  
                    change = inserted_money - drink_cost
                    
                    if change > 0:
                        print(f"Here is Rs. {change} in change.")
                        
                    make_coffee(choice, drink["ingredients"])  
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    
        case "owner":
            password = input("🔑 Enter Owner Password: ").strip()
            
            if password == OWNER_PASSWORD:
                print("\n🔓 Access Granted. Opening Maintenance Panel...")
                admin_choice = input("👉 Context commands: 'report' / 'refill' / 'off'\nChoice: ").lower().strip()
                
                match admin_choice:
                    case "report":  
                        print_report()
                    case "refill":  
                        refill_resources()
                    case "off":     
                        print("Shutting down the machine. Goodbye!")
                        machine_on = False
                    case _:
                        print("Invalid admin command. Exiting owner panel.")
            else:
                print("❌ Incorrect password! Returning to standard menu.")
                
        case _:
            print("Invalid selection. Please choose an item from the menu.")
