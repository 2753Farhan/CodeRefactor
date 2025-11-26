import pandas as pd

from pandas.io.formats.style import Styler

def process_data(item, price):
    # Cleanse data
    item = item.strip()  # Strip whitespace from item
    price = price.strip()  # Strip whitespace from price
    price = float(price) # Convert price to a float
    # More cleansing operations here

    # Create and print a DataFrame
    data = {'Item': [item], 'Price': [price]}
    df = pd.DataFrame(data)
    print(df.to_string(index=False))

# Example usage
item = "   Apple "
price = " 1.25"
process_data(item, price)
