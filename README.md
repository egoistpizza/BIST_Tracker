# BIST Tracker

BIST Tracker is a Python project designed to scrape and store real-time stock data from Borsa Istanbul (BIST). It periodically retrieves data from a specified URL and saves it into a CSV file for further analysis or integration with other systems.

## Installation

To use BIST Tracker, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/egoistpizza/BIST-Tracker.git
   cd BIST-Tracker

2. Install the required Python packages. It's recommended to use a virtual environment:

   ```bash
   pip install -r requirements.txt

## Usage

1. Run the main.py script:

   ```bash
   python main.py
   ```
   
   This will start the data scraping process. The script will fetch stock symbols, daily changes, and prices from the specified URL and store them in a CSV file (BIST.csv).


2. The data will be updated every 5 minutes (300 seconds) by default, as specified in the script (time.sleep(300)). You can adjust this interval according to your needs.

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

### Pull Requests

1. Fork the repository and create your branch from `master`.
2. Make your changes and test thoroughly.
3. Ensure your code follows the project's coding style and conventions.
4. Update documentation if necessary.
5. Issue a pull request describing your changes.

### Issues

If you encounter any issues with the project or have suggestions for improvements, please check the existing issues on GitHub. If your issue is not addressed, you can open a new one:

1. Go to the [Issues](https://github.com/egoistpizza/BIST_Tracker/issues) section on GitHub.
2. Click on the "New Issue" button.
3. Provide a descriptive title and detailed description of the issue or suggestion.

Your feedback helps us improve this project for everyone!

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

BIST Tracker is provided as-is without any warranty. It is intended for educational and informational purposes only. Users are responsible for compliance with applicable laws and regulations while using this software.

---

© Copyright 2024 egoistpizza
