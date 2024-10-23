import os
import requests

api_key = "33sNVpBCyamfipIlSItccQ==8edrp7Ho60xWLsrK"
url = "https://api.api-ninjas.com/v1/animals?name="
headers = {
    "X-API-Key": api_key
}

# Get user input for the animal name
animal_name = input(
    "Enter the name of the animal you want to search for: "
)  # User input for animal name
res = requests.get(url + animal_name, headers=headers)

# Global variable for animal data
animals_data = []

# Check if the request was successful
if res.status_code == 200:
    animals_data = res.json()
    if not animals_data:  # Check if any data is returned
        print(f"<h2>The animal '{animal_name}' doesn't exist.</h2>")
        exit()
else:
    print(f"<h2>The animal '{animal_name}' doesn't exist.</h2>")
    exit()


def main():
    output = ""
    for animal in animals_data:
        if "characteristics" in animal and "type" in animal["characteristics"]:
            name = animal["name"]
            diet = animal["characteristics"]["diet"]
            animal_type = animal["characteristics"]["type"]
            locations = animal["locations"][0] if animal["locations"] else "N/A"
            output += '<li class="cards__item">\n'
            output += f"<div class='card__title'>{name}</div>\n"
            output += (
                f"<p class='card__text'><strong>Diet:</strong> {diet}<br/>\n"
            )
            output += f"<strong>Location:</strong> {locations}<br/>\n"
            output += f"<strong>Type:</strong> {animal_type}<br/>\n"
            output += "</p></li>\n"

    # Construct the file path
    try:
        template_file_path = os.path.join(
            os.path.dirname(__file__), "animals_template.html"
        )
        with open(template_file_path, "r") as html_file:
            html_content = html_file.read()
    except FileNotFoundError:
        print("Error: The template HTML file was not found.")
        return

    # Replace the placeholder with the output
    modified_html = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # Save the modified HTML to a new file
    with open("animals.html", "w") as modified_file:
        modified_file.write(modified_html)


if __name__ == "__main__":
    main()
