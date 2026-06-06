import coffie_logo

# Display the logo when the machine turns on
print(coffie_logo.logo)

# The menu dictionary with updated 2026 cafe prices (in Rupees)
menu = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250  # Updated present price
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150  # Updated present price
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 220  # Updated present price
    }
}

# The initial resources dictionary (increased slightly so you can test more orders!)
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
}

# Global variable to track the money made
profit = 0