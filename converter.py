import requests

VALID_CURRENCIES = [
    "USD", "EUR", "GBP", "ZAR", "CHF", "JPY",
    "CAD", "AUD", "NZD", "CNY", "INR"
]

def convert_currency():
    base = input("Enter base currency (e.g. USD): ").upper()
    target = input("Enter target currency (e.g. EUR): ").upper()

    if base not in VALID_CURRENCIES or target not in VALID_CURRENCIES:
        print("❌ Invalid currency code. Use standard 3-letter codes.")
        return

    amount_input = input("Enter amount to convert: ")

    try:
        amount = float(amount_input)
    except ValueError:
        print("❌ Invalid amount. Must be a number.")
        return

    url = f"https://api.frankfurter.app/latest?amount={amount}&from={base}&to={target}"
    response = requests.get(url)

    print("DEBUG: HTTP", response.status_code)
    print("DEBUG: Raw response:", response.text)

    if response.status_code != 200:
        print("❌ Could not fetch exchange rate.")
        return

    try:
        data = response.json()
        result = data["rates"].get(target)
        if result is None:
            print("❌ Target currency not found in response.")
            return

        print(f"\n✅ {amount:.2f} {base} = {result:.2f} {target}")

    except Exception as e:
        print("❌ Failed to parse response:", e)

if __name__ == "__main__":
    convert_currency()