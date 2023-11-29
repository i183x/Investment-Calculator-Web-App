# Investment Calculator Web App

## Overview

This web application provides a user-friendly interface for calculating investment returns based on user-input parameters such as lump sum amount, compound annual growth rate (CAGR), investment duration, and yearly addition. The application is built using Flask, a Python web framework.

## Features

- **User-Friendly Interface:** The web app offers a clean and intuitive interface for users to input their investment details.

- **Real-Time Calculation:** As users input their investment parameters, the application dynamically calculates and displays the net amount and total profit, providing instant feedback.

- **Formatted Output:** The results are presented in a visually appealing format with Indian-style number formatting for better readability.

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

### Running the App

Execute the following command to run the Flask web application:

```bash
python3 app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your web browser to access the Investment Calculator.

## Usage

1. Enter the lump sum amount, CAGR (in percentage), number of years, and yearly addition in the provided form.

2. Click the "Calculate" button to see the calculated net amount and total profit after the specified investment duration.

## File Structure

- **app.py:** The main Python script containing the Flask application and investment calculation logic.

- **requirements.txt:** A file specifying the Python dependencies required to run the application.

- **templates/index.html:** The HTML template for the web interface.

## Dependencies

- Flask 3.0.0
- python-dateutil 2.8.2

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and suggestions are highly appreciated.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Flask for providing a simple and powerful framework for web development in Python.
- Special thanks to the contributors and the open-source community.
