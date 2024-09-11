import random

# Predefined phrases for chatbot responses
greetings = ["Hello!", "Hi there!", "Greetings!", "Hey!"]
farewells = ["Goodbye!", "See you later!", "Take care!", "Bye!"]
general_responses = [
    "That's interesting!",
    "Tell me more!",
    "I see.",
    "I'm here to listen.",
]

# Simulated weather data using a dictionary
weather_data = {
    "Kathmandu": "Sunny, 25°C",
    "Pokhara": "Cloudy, 22°C",
    "Biratnagar": "Rainy, 27°C",
    "Chitwan": "Sunny, 30°C"
}

# Math operations
def math_operations():
    print("\nYou can ask me to perform simple math operations.")
    print("Options: Add, Subtract, Multiply, Divide")
    operation = input("Enter the operation: ").lower()
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            result = num1 / num2 if num2 != 0 else "undefined (division by zero)"
        else:
            print("Invalid operation.")
            return
        
        print(f"The result of the operation is: {result}\n")
    except ValueError:
        print("Invalid input. Please enter numeric values.\n")

# Function to simulate a conversation
def general_conversation():
    print("\nLet's have a conversation! You can type 'exit' anytime to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print(random.choice(farewells))
            break
        else:
            print(f"Chatbot: {random.choice(general_responses)}")

# Function to provide weather info
def weather_info():
    print("\nI can provide the weather forecast for major cities in Nepal.")
    city = input("Enter the city name (Kathmandu, Pokhara, Biratnagar, Chitwan): ")
    
    weather = weather_data.get(city.capitalize(), "Sorry, I don't have weather information for that city.")
    print(f"Weather in {city.capitalize()}: {weather}\n")

# Main chatbot function
def chatbot():
    print(random.choice(greetings))
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!\n")

    while True:
        print("What would you like to do?")
        print("1. Have a conversation")
        print("2. Get weather information")
        print("3. Perform math operations")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            general_conversation()
        elif choice == "2":
            weather_info()
        elif choice == "3":
            math_operations()
        elif choice == "4":
            print(random.choice(farewells))
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
