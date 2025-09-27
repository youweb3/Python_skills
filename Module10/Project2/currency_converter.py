import exchange_rates

comition_fee = 0.5 #Global variable


def apply_commission(amount, rate):

    print(f"Applying commission fee of {comition_fee} USD")
    return (amount * rate) - comition_fee

def convert_usd_euro(amount):
    return apply_commission(amount, exchange_rates.USD_TO_EUR)

def convert_usd_to_gbp(amount):
    return apply_commission(amount, exchange_rates.USD_TO_GBP)

def convert_usd_to_yen(amount):
    return apply_commission(amount, exchange_rates.USD_TO_Yen)
    

#test the function
# Main function
def main():
  amount = float(input("Enter amount in USD: "))

  print(f"USD to EUR: {convert_usd_euro(amount)}")
  print(f"USD to GBP: {convert_usd_to_gbp(amount)}")
  print(f"USD to JPY: {convert_usd_to_yen(amount)}")


# This ensures main() runs only when the file is executed directly
if __name__ == "__main__":
 main()