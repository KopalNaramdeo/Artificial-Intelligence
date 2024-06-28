# Dictionary mapping cities in India to their descriptions
city_info = {
    "delhi": "Delhi is the capital city of India and is known for its rich history, diverse culture, and iconic landmarks such as the Red Fort, India Gate, and Qutub Minar.",
    "mumbai": "Mumbai, formerly known as Bombay, is the financial capital of India and is famous for its bustling streets, Bollywood film industry, and historic landmarks like the Gateway of India.",
    "kolkata": "Kolkata, formerly known as Calcutta, is the cultural capital of India and is renowned for its art, literature, and festivals. It is home to landmarks like the Victoria Memorial and Howrah Bridge.",
    "chennai": "Chennai, formerly known as Madras, is the capital city of the Indian state of Tamil Nadu. It is known for its vibrant culture, classical music, and Marina Beach, one of the longest urban beaches in the world.",
    "bangalore": "Bangalore, officially known as Bengaluru, is the capital city of the Indian state of Karnataka. It is known as the 'Silicon Valley of India' due to its thriving IT industry and is also famous for its pleasant climate and green spaces.",
}

# Function to provide information about cities in India
def city_info_lookup(city):
    return city_info.get(city.lower(), "Sorry, I don't have information about that city in India.")

# Function for interacting with the city information catboat
def interact():
    print("Welcome to Indian City Information Assistant! You can ask me for information about different cities in India.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Indian City Information Assistant: Goodbye! Have a great day!")
            break
        else:
            info = city_info_lookup(user_input)
            print("Indian City Information Assistant:", info)

if __name__ == "__main__":
    interact()
