import os
from data_fetcher import fetch_data
from animals_web_generator import generate_html

def main():
    # Get user input for the animal name
    animal_name = input("Please enter an animal: ").lower()
    
    # Fetch data using data_fetcher
    animals_data = fetch_data(animal_name)
    if not animals_data:
        print(f"<h2>The animal {animal_name} doesn't exist.</h2>")
        exit()

    # Load the template HTML file
    template_path = os.path.join(os.path.dirname(__file__), "animals_template.html")
    try:
        with open(template_path, "r") as template_file:
            html_content = template_file.read()
    except FileNotFoundError:
        print("Error: The template HTML file was not found.")
        return

    # Generate HTML content and replace the placeholder
    modified_html = html_content.replace("__REPLACE_ANIMALS_INFO__", generate_html(animals_data))
    
    # Save the modified HTML to a new file
    with open("animals.html", "w") as output_file:
        output_file.write(modified_html)
    print("Website generated successfully!")

if __name__ == "__main__":
    main()