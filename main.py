import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        if "type" in animal["characteristics"]:
            name = animal["name"]
            diet = animal["characteristics"]["diet"]
            animal_type = animal["characteristics"]["type"]
            locations = animal["locations"][0]
            print(f"Name: {name}\nDiet: {diet}\nLocation: {locations}\nType: {animal_type}\n")


if __name__ == "__main__":
    main()