import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")
    output = ""
    for animal in animals_data:
        if "type" in animal["characteristics"]:
            name = animal["name"]
            diet = animal["characteristics"]["diet"]
            animal_type = animal["characteristics"]["type"]
            locations = animal["locations"][0]
            output += '<li class="cards__item">\n'
            output += f"<div class='card__title'>{name}</div>\n"
            output += f"<p class='card__text'><strong>Diet:</strong> {diet}<br/>\n"
            output += f"<strong>Location:</strong> {locations}<br/>\n"
            output += f"<strong>Type:</strong> {animal_type}<br/>\n"
            output += "</p></li>\n"

    with open("animals_template.html", "r") as html_file:
        html_content = html_file.read()

    modified_html = html_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w") as modified_file:
        modified_file.write(modified_html)


if __name__ == "__main__":
    main()