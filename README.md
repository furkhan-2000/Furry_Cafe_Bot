**Project Overview**: -

The Furry Café chatbot is a simple web application built using Flask for the backend, HTML/CSS/JavaScript for the frontend, and AWS Lambda for handling the chatbot responses. The application allows users to interact with the chatbot through a webpage, which communicates with the Lambda function to handle requests like greetings, menu display, orders, and general queries.

**structure of Furry Cafe:** 
        
 furrybot/               # Project DIR
├── app.py               # Flask application
├── templates/           # UI DIR
│   └── index.html       # Frontend HTML file
├── venv/                # Python virtual environment
│   ├── bin/
│   ├── include/
│   ├── lib/
│   ├── lib64/
│   └── pyvenv.cfg

**Summary:**

*Backend*: Flask serves the webpage and communicates with the Lambda function.
*Frontend*: A simple HTML page allows user interaction.
*AWS Lambda*: Handles chatbot responses with predefined logic

##### Install Python and Virtual Environment
   python3 -m venv venv
   source venv/bin/activate  # Activate the virtual environment 

   ###### Install Dependencies:
   pip install flask requests 


the possible outcomes or cases of user interaction with the Furry Café chatbot, along with expected responses from the bot:

   ###### 1. Greeting the Bot
User Input:

"Hi"
"Hello"
"Hey"
Bot Response:

"Welcome to Furry Café – where every sip and bite is crafted to delight. We're thrilled to have you with us! ☕🍰"
###### 2. Requesting the Menu
User Input:

"Show me the menu"
"What do you have?"
"Menu"
Bot Response:

"What would you like to have? 😋 We serve:
Tea 🍵
Coffee ☕
Desserts 🍩
Smoothies 🥤
Bites 🍔"
###### 3. Asking for a Specific Category
User Input:

"Tea"
"Coffee"
"Desserts"
Bot Response:

For Tea:
"Here are our teas:
Green Tea
Black Tea
Jasmine Tea
Oolong Tea
Chamomile Tea"

For Coffee:
"Here are our coffees:
Arabic Coffee (Qahwa)
Saudi Coffee (Gahwa)
Yemeni Coffee (Mocha)
Espresso Freddo
Cappuccino
Freddo Cappuccino
Americano
Latte
Flat White
Affogato
Macchiato"
For Desserts:
"Here are our desserts:
Chocolate Cake
Cheesecake
Tiramisu
Macarons
Brownies"

###### 4. Making an Order
User Input:

"I'd like to order a Cappuccino"
"Can I get a Chocolate Cake?"
Bot Response:

For Cappuccino:

"Thank you for your patience. Your Cappuccino is being prepared with the utmost care 💖 and will be arriving shortly 🚚. We appreciate your understanding and look forward to serving you soon. 🎉"
For Chocolate Cake:

"Thank you for your patience. Your Chocolate Cake is being prepared with the utmost care 💖 and will be arriving shortly 🚚. We appreciate your understanding and look forward to serving you soon. 🎉"
###### 5. Asking for the Location

User Input:

"Where are you located?"
"What is your address?"
"Location"

Bot Response:

"We are located at: 9-10-99, Jubilee Hills Road no 36, Above Khan Manzil, Hyderabad, Telangana 🌟."
6. Asking for Contact Information
User Input:

"How can I contact you?"
"Give me your phone number"
"Contact info"
Bot Response:

"You can reach us here: 📧 Email: support@furrycafe.com 📞 Phone: +1 (555) 456-7896"
###### 7. Unrecognized Input (Error Handling)
User Input:

"I want a pizza"
"What’s your favorite color?"
Bot Response:

"I'm sorry, I didn't quite understand that. Here's what I can help you with:
View our menu 🍽️
Place an order 🛒
Provide feedback 💬 Just let me know how I can assist you! 😊"

###### 8. Empty or Invalid Input
User Input:

(No message)
Just pressing "Send" with an empty input
Bot Response:

"It seems like you didn't type anything. Could you please provide more details?"

###### 9. Handling Unexpected Errors
User Input:

Any input that causes an internal error (e.g., server issues or unhandled exceptions)
Bot Response:

"An unexpected error occurred. Please try again later."
Summary of Key Interactions:
Greetings: The bot responds with a warm welcome message.
Menu Request: Displays available menu items for food and drinks.
Order Request: Confirms the order and provides a friendly confirmation message.
Location/Contact Inquiry: Shares the café's address and contact details.
Unrecognized Input: Provides an error message with instructions on what the user can ask.
Empty Input: Prompts the user to provide more details or make a selection.
Error Handling: If the bot encounters an issue, it gracefully returns an error message.


