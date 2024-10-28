
# My Zootopia

**My Zootopia** is a Python-based application that prompts users for an animal name, retrieves information about that animal from the [API-NINJAS](https://api-ninjas.com/) API, and dynamically generates an HTML file based on a pre-defined template. This HTML file provides a structured display of animal information, making it easy to explore various species.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)

## Features
- **User Input**: Users provide an animal name to search.
- **API Integration**: Utilizes the API-NINJAS API to retrieve detailed information about the specified animal.
- **HTML Generation**: Dynamically creates an HTML file using a template to present animal information in a user-friendly format.

## Getting Started

### Prerequisites
- **Python 3.x**: Ensure Python is installed. Download it [here](https://www.python.org/downloads/).
- **API Key for API-NINJAS**: Register and obtain an API key from [API-NINJAS](https://api-ninjas.com/).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Kurosuisho/My-Zootopia.git
   cd My-Zootopia
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your API Key:
   - Create a `.env` file in the root directory.
   - Add the following line to the `.env` file:
     ```plaintext
     API_NINJAS_KEY=your_api_key_here
     ```

## Usage
1. Run the main Python script:
   ```bash
   python main.py
   ```
2. Enter the name of an animal when prompted.
3. The program will:
   - Search for the specified animal on API-NINJAS.
   - Generate an HTML file in the output directory based on the information retrieved.
4. Open the generated HTML file to view the animal information.

### Example
```plaintext
$ python main.py
Enter the name of an animal: Lion
```

Upon completion, an HTML file (e.g., `Lion.html`) will be generated with details about the animal.

## Contributing
To contribute to **My Zootopia**, please follow these guidelines:

### Reporting Bugs
- Ensure the bug hasn't already been reported by reviewing the [Issues](https://github.com/Kurosuisho/My-Zootopia/issues) section.
- Provide a clear and concise description of the issue.
- Include details on how to reproduce the issue and, if possible, attach screenshots or logs.

### Requesting Features
- Review the [Issues](https://github.com/Kurosuisho/My-Zootopia/issues) section to ensure the feature hasn’t been requested.
- Create a new issue with the feature request, including details on its purpose and benefits.

### Pull Requests
1. Fork the repository and clone it locally.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add feature: YourFeatureName"
   ```
4. Push to your fork and create a pull request:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Ensure your pull request includes a clear description of your changes.
