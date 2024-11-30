import json
import re

# Predefined responses
responses = {
    "greeting": {
        "text": "Welcome to Furry Café – where every sip and bite is crafted to delight. We're thrilled to have you with us! ☕🍰",
        "buttons": None
    },
    "menu_prompt": {
        "text": "What would you like to have? 😋\nWe serve:\n1. Tea 🍵\n2. Coffee ☕\n3. Desserts 🍩\n4. Smoothies 🥤\n5. Bites 🍔",
        "buttons": None
    },
    "order_confirmation": {
        "text": "Thank you for your patience. Your [item] is being prepared with the utmost care 💖 and will be arriving shortly 🚚. We appreciate your understanding and look forward to serving you soon. 🎉",
        "buttons": None
    },
    "error": {
        "text": "I'm sorry, I didn't quite understand that. Here's what I can help you with:\n- View our menu 🍽️\n- Place an order 🛒\n- Provide feedback 💬\nJust let me know how I can assist you! 😊",
        "buttons": None
    },
    "location": {
        "text": "We are located at:\n9-10-99, Jubilee Hills Road no 36,\nAbove Khan Manzil,\nHyderabad, Telangana 🌟.",
        "buttons": None
    },
    "contact": {
        "text": "You can reach us here:\n📧 Email: support@furrycafe.com\n📞 Phone: +1 (555) 456-7896",
        "buttons": None
    }
}

# Menu items and subcategories
menu_items = {
    "tea": ["Green Tea", "Black Tea", "Jasmine Tea", "Oolong Tea", "Chamomile Tea"],
    "coffee": ["Arabic Coffee (Qahwa)", "Saudi Coffee (Gahwa)", "Yemeni Coffee (Mocha)", "Espresso Freddo", "Cappuccino", "Freddo Cappuccino", "Americano", "Latte", "Flat White", "Affogato", "Macchiato"],
    "desserts": ["Chocolate Cake", "Cheesecake", "Tiramisu", "Macarons", "Brownies"],
    "smoothies": ["Mango Smoothie", "Berry Blast Smoothie", "Tropical Delight Smoothie", "Green Detox Smoothie", "Chocolate Banana Smoothie"],
    "bites": ["Chicken Sandwich", "Veggie Wrap", "Beef Burger", "Cheese Croissant", "Quiche"]
}

# Main Lambda handler function
def lambda_handler(event, context):
    try:
        # Validate the event structure
        if 'body' not in event:
            raise ValueError("Missing body in the event.")
        
        body = json.loads(event['body'])
        
        if 'message' not in body:
            raise ValueError("Missing 'message' in the body.")
        
        user_message = body.get('message', '').lower()

        # Ensure the message is not empty
        if not user_message.strip():
            return generate_error_response("It seems like you didn't type anything. Could you please provide more details?")

        # Handle user input
        response = handle_user_input(user_message)

        # Format and return the chatbot response
        formatted_response = {
            "response_text": response["text"],
            "response_buttons": response["buttons"]
        }

        return {
            "statusCode": 200,
            "body": json.dumps(formatted_response),
            "headers": {"Content-Type": "application/json"}
        }
    except ValueError as ve:
        return generate_error_response(str(ve))
    except json.JSONDecodeError:
        return generate_error_response("There was an issue processing the data. Please try again.")
    except Exception as e:
        return generate_error_response(f"An unexpected error occurred: {str(e)}")

# Function to handle user input
def handle_user_input(user_message):
    # Check for greetings
    if user_message in ['hi', 'hello', 'hey']:
        return responses["greeting"]

    # Check for menu request
    if 'menu' in user_message or 'show' in user_message:
        return responses["menu_prompt"]

    # Check for order keyword
    if "order" in user_message:
        return handle_order(user_message)

    # Check for submenu requests
    for category in menu_items.keys():
        if category in user_message:
            return {
                "text": f"Here are our {category}s:\n" + "\n".join([f"{i + 1}. {item}" for i, item in enumerate(menu_items[category])]),
                "buttons": None
            }

    # Check for location/address keywords
    if any(keyword in user_message for keyword in ['location', 'address']):
        return responses["location"]

    # Check for contact details
    if any(keyword in user_message for keyword in ['contact', 'phone', 'email']):
        return responses["contact"]

    # Handle unrecognized input
    return responses["error"]

# Function to handle orders
def handle_order(user_message):
    for category, items in menu_items.items():
        for item in items:
            if re.search(r'\b' + re.escape(item.lower()) + r'\b', user_message):
                response = responses["order_confirmation"]
                response["text"] = response["text"].replace("[item]", item)
                return response

    # If no matching item found
    return {
        "text": "I'm sorry, I couldn't find the item you're trying to order. Please check the menu and try again. 😊",
        "buttons": None
    }

# Error handling function
def generate_error_response(message):
    return {
        "statusCode": 400,
        "body": json.dumps({
            "response_text": message,
            "response_buttons": None
        }),
        "headers": {"Content-Type": "application/json"}
    }
