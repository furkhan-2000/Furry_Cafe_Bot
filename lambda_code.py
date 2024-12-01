import json
import re

# Predefined responses
responses = {
    "greeting": {"text": "Welcome to Furry Café – where every sip and bite is crafted to delight. We're thrilled to have you with us! ☕🍰", "buttons": None},
    "menu_prompt": {"text": "What would you like to have? 😋\nWe serve:\n1. Tea 🍵\n2. Coffee ☕\n3. Desserts 🍩\n4. Smoothies 🥤\n5. Bites 🍔", "buttons": None},
    "order_confirmation": {"text": "Thank you for your patience. Your order of [items] is being prepared with the utmost care 💖 and will arrive shortly 🚚.", "buttons": None},
    "cancel_confirmation": {"text": "Your order has been successfully canceled. Let us know if you'd like to place a new order! 😊", "buttons": None},
    "replace_confirmation": {"text": "Your order has been updated to: [items]. It will be prepared with care 💖 and delivered shortly. 🎉", "buttons": None},
    "error": {"text": "I'm sorry, I didn't quite understand that. Here's what I can help you with:\n- View our menu 🍽️\n- Place an order 🛒\n- Provide feedback 💬\nJust let me know how I can assist you! 😊", "buttons": None},
    "location": {"text": "We are located at:\n9-10-99, Jubilee Hills Road no 36, Above Khan Manzil, Hyderabad, Telangana 🌟.", "buttons": None},
    "contact": {"text": "You can reach us here:\n📧 Email: support@furrycafe.com\n📞 Phone: +1 (555) 456-7896", "buttons": None},
}

# Menu items and subcategories
menu_items = {
    "tea": ["Green Tea", "Black Tea", "Jasmine Tea", "Oolong Tea", "Chamomile Tea"],
    "coffee": ["Arabic Coffee", "Saudi Coffee", "Yemeni Coffee", "Espresso Freddo", "Cappuccino", "Americano", "Latte", "Flat White", "Affogato", "Macchiato"],
    "desserts": ["Chocolate Cake", "Cheesecake", "Tiramisu", "Macarons", "Brownies"],
    "smoothies": ["Mango Smoothie", "Berry Blast Smoothie", "Tropical Delight Smoothie", "Green Detox Smoothie", "Chocolate Banana Smoothie"],
    "bites": ["Chicken Sandwich", "Veggie Wrap", "Beef Burger", "Cheese Croissant", "Quiche"],
}

# Global variable to track the current order
current_order = []

# Main Lambda handler function
def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        user_message = body.get("message", "").strip().lower()

        if not user_message:
            return generate_error_response("It seems like you didn't type anything. Could you please provide more details?")

        response = handle_user_input(user_message)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "response_text": response["text"],
                "response_buttons": response["buttons"],
            }),
            "headers": {"Content-Type": "application/json"},
        }
    except json.JSONDecodeError:
        return generate_error_response("There was an issue processing the data. Please try again.")
    except Exception as e:
        return generate_error_response(f"An unexpected error occurred: {str(e)}")

# Function to handle user input
def handle_user_input(user_message):
    global current_order

    # Check for greetings
    if user_message in ["hi", "hello", "hey"]:
        return responses["greeting"]

    # Check for menu request
    if "menu" in user_message or "show" in user_message:
        return responses["menu_prompt"]

    # Check for specific category requests
    for category in menu_items:
        if category in user_message:
            items_list = menu_items[category]
            return {
                "text": f"Here are our {category}s:\n" + "\n".join([f"{i + 1}. {item}" for i, item in enumerate(items_list)]),
                "buttons": None,
            }

    # Check for cancel order
    if "cancel" in user_message:
        return handle_cancel_order()

    # Check for replace order
    if "replace" in user_message or "change" in user_message:
        return handle_replace_order(user_message)

    # Check for new order
    if "order" in user_message:
        return handle_order(user_message)

    # Handle unrecognized input
    return responses["error"]

# Function to handle orders
def handle_order(user_message):
    global current_order

    matches = match_menu_item(user_message)
    if matches:
        # Clear any previous orders before placing a new one
        current_order = matches
        items_str = ", ".join(current_order)
        response = responses["order_confirmation"]
        response["text"] = response["text"].replace("[items]", items_str)
        return response

    return suggest_items(user_message)

# Function to cancel orders
def handle_cancel_order():
    global current_order

    if current_order:
        current_order.clear()  # Clear the current order
        return responses["cancel_confirmation"]

    return {
        "text": "You don't have any active orders to cancel. Let us know if you'd like to place a new one! 😊",
        "buttons": None,
    }

# Function to replace orders
def handle_replace_order(user_message):
    global current_order

    # Clear the current order before replacing it
    current_order.clear()

    matches = match_menu_item(user_message)
    if matches:
        current_order = matches  # Replace current order
        items_str = ", ".join(current_order)
        response = responses["replace_confirmation"]
        response["text"] = response["text"].replace("[items]", items_str)
        return response

    return suggest_items(user_message)

# Match user input to menu items
def match_menu_item(user_message):
    matches = []
    for category, items in menu_items.items():
        for item in items:
            if re.search(rf"\b{re.escape(item.lower())}\b", user_message):
                matches.append(item)
    return matches

# Suggest closest matches
def suggest_items(user_message):
    suggestions = []
    for category, items in menu_items.items():
        for item in items:
            if any(word in item.lower() for word in user_message.split()):
                suggestions.append(item)

    if suggestions:
        return {
            "text": "I'm sorry, I couldn't process your exact order. Did you mean one of these?\n" + "\n".join(suggestions),
            "buttons": None,
        }

    return {
        "text": "I'm sorry, I couldn't find any items related to your input. Please check the menu and try again. 😊",
        "buttons": None,
    }

# Generate error response
def generate_error_response(message):
    return {
        "statusCode": 400,
        "body": json.dumps({
            "response_text": message,
            "response_buttons": None,
        }),
        "headers": {"Content-Type": "application/json"},
    }
