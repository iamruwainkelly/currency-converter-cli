def convert_currency():
    try:
        rate = float(input("Enter conversion rate (e.g. 18.39 for USD to ZAR): "))
        amount = float(input("Enter amount to convert: "))
        converted = rate * amount
        print(f"Converted amount: {converted:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    convert_currency()