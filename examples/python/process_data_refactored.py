import pandas as pd

# Refactored: split cleansing and printing into two functions

def cleanse_data(item, price):
    item = item.strip()
    price = price.strip()
    price = float(price)
    return item, price


def print_data(item, price):
    data = {'Item': [item], 'Price': [price]}
    df = pd.DataFrame(data)
    print(df.to_string(index=False))


def process_data(item, price):
    item, price = cleanse_data(item, price)
    print_data(item, price)

# Example usage
if __name__ == "__main__":
    process_data("   Apple ", " 1.25")
