
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('API_KEY')
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal "animal_name".
    Returns: a list of animals, each animal is a dictionary.
    """
    
    # Full URL for the API request
    api_url = BASE_URL + animal_name

    # Headers for the request
    headers = {
        "X-API-Key": API_KEY
    }

    try:
        # Send GET request to the API
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Return JSON response if the call was successful
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return []  # Return an empty list if there was an error
