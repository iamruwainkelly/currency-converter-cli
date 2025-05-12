# 💱 Currency Converter CLI

A simple Python command-line tool to convert currencies using real-time exchange rates from the [Frankfurter API](https://www.frankfurter.app/). No API key required.

---

## Features

- Convert any amount between supported currencies
- Uses real, live exchange rates
- Validates input formats
- Works entirely in your terminal
- Lightweight, fast, and easy to use

---

## Requirements

- Python 3.8 or higher
- `requests` library (install via pip)

---

## Setup Instructions

```bash
# Clone the repo
git clone https://github.com/iamruwainkelly/currency-converter-cli.git
cd currency-converter-cli

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install requests

# Run the app
python converter.py

Supported Currencies
	•	USD – US Dollar
	•	EUR – Euro
	•	GBP – British Pound
	•	ZAR – South African Rand
	•	CHF – Swiss Franc
	•	JPY – Japanese Yen
	•	CAD – Canadian Dollar
	•	AUD – Australian Dollar
	•	NZD – New Zealand Dollar
	•	CNY – Chinese Yuan
	•	INR – Indian Rupee

⸻

🛠 Example Usage

Enter base currency (e.g. USD): EUR
Enter target currency (e.g. ZAR): USD
Enter amount to convert: 100

✅ 100.00 EUR = 107.35 USD

Author

Developed by Ruwain Kelly
🇿🇦 Built with passion and purpose

⸻

📜 License

This project is licensed under the MIT License.

