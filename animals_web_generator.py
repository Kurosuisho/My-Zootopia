
import os
import data_fetcher  # Import data_fetcher for fetching data

def generate_html(animals):
    """Generates HTML list items for each animal."""
    output = ""
    for animal in animals:
        characteristics = animal.get("characteristics", {})
        name = animal.get("name", "Unknown")
        diet = characteristics.get("diet", "N/A")
        animal_type = characteristics.get("type", characteristics.get("group", "N/A"))
        locations = animal.get("locations", ["N/A"])[0]
        
        output += (
            f"<li class=\"cards__item\">\n"
            f"<div class=\"card__title\">{name}</div>\n"
            f"<p class=\"card__text\"><strong>Diet:</strong> {diet}<br/>\n"
            f"<strong>Location:</strong> {locations}<br/>\n"
            f"<strong>Type:</strong> {animal_type}<br/>\n</p></li>\n"
        )
    return output
