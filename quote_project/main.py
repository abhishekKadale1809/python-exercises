# main.py

# Import the get_random_quote function from the api_handler file.
from api_handler import get_random_quote

# Call the function and store the result in a variable named 'quote'.
quote = get_random_quote()

# Print the final quote
print("--- Your Inspirational Quote of the Day ---")
print(quote)
