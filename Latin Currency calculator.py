#Creatiing currency converter for colobian pesos to us dollars
#peruvian soles to us dollars
#brazilian reais to us dollars

#First we need to get the exchange rates from the internet 

rate_cop_to_usd = 1 / 4115 
rate_pen_to_usd = 1 / 3.61
rate_brl_to_usd = 1 / 5.58

#Now we need to get the leftover currency from the user

cop_leftover = float(input('What do you have left in Colombian pesos? '))
pen_leftover = float(input('What do you have left in Peruvian soles? '))
brl_leftover = float(input('What do you have left in Brazilian reais? '))

# Sum all the leftover currency

total_usd = usd_from_cop + usd_from_pen + usd_from_brl

#Print the results

print(f'$ {total_usd:.2f}')

#Now we need to convert the leftover currency to us dollarsss

usd_from_cop = cop_leftover * rate_cop_to_usd
usd_from_pen = pen_leftover * rate_pen_to_usd
usd_from_brl = brl_leftover * rate_brl_to_usd
print(f'USD from COP: ${usd_from_cop:.2f}')
print(f'USD from PEN: ${usd_from_pen:.2f}')
print(f'USD from BRL: ${usd_from_brl:.2f}')

# Add a breakdown table for clarity
print("\nBreakdown Table:")
print("{:<20} {:<20} {:<20}".format("Currency", "Amount Leftover", "USD Equivalent"))
print("{:<20} {:<20.2f} ${:<19.2f}".format("Colombian Pesos", cop_leftover, usd_from_cop))
print("{:<20} {:<20.2f} ${:<19.2f}".format("Peruvian Soles", pen_leftover, usd_from_pen))
print("{:<20} {:<20.2f} ${:<19.2f}".format("Brazilian Reais", brl_leftover, usd_from_brl))
print("-" * 60)
print("{:<20} {:<20} ${:<19.2f}".format("TOTAL", "", total_usd))

# Add a feature to save the results to a file
save = input("\nWould you like to save this breakdown to a file? (y/n): ").strip().lower()
if save == 'y':
    filename = input("Enter filename (e.g., results.txt): ").strip()
    with open(filename, "w") as f:
        f.write("Breakdown Table:\n")
        f.write("{:<20} {:<20} {:<20}\n".format("Currency", "Amount Leftover", "USD Equivalent"))
        f.write("{:<20} {:<20.2f} ${:<19.2f}\n".format("Colombian Pesos", cop_leftover, usd_from_cop))
        f.write("{:<20} {:<20.2f} ${:<19.2f}\n".format("Peruvian Soles", pen_leftover, usd_from_pen))
        f.write("{:<20} {:<20.2f} ${:<19.2f}\n".format("Brazilian Reais", brl_leftover, usd_from_brl))
        f.write("-" * 60 + "\n")
        f.write("{:<20} {:<20} ${:<19.2f}\n".format("TOTAL", "", total_usd))
    print(f"Results saved to {filename}.")

# Add a feature to show the date and time of conversion
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# The code above calculates the USD equivalent of leftover Latin American currencies.
# It prints a breakdown table and optionally saves the results to a file.
# The date and time of the conversion are also displayed for record-keeping.

# The code below is well-commented to help you understand each step.
# If you want to add more currencies, simply follow the pattern for input, conversion, and table display.
# You can also adjust the exchange rates at the top of your script for up-to-date values.
# The breakdown table provides a clear summary of your leftover currency and their USD equivalents.
# Saving to a file allows you to keep a record of your conversions for future reference.
# The date and time stamp ensures you know exactly when the conversion was performed.
# If you have suggestions for more features (like fetching live rates), you can expand this script further!
# Small feature: Ask user if they want to clear the screen before exiting
import os
clear_screen = input("\nClear the screen before exiting? (y/n): ").strip().lower()
if clear_screen == 'y':
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Thank you for using the Latin Currency Calculator. Goodbye!")
    input("Press Enter to exit...")
    exit()

# Add a feature to show the date and time of conversion
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add a feature to show the date and time of conversion
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add a feature to show the date and time of conversion
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add a feature to show the date and time of conversion
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Add a feature to show the date and time of conversi
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
#here is the code for the currency converterr

# Add a feature to show the date and time of conversion
from datetime import datetime
print(f"\nConversion performed on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}") 
# The repeated blocks below display the date and time of the conversion.
# Each block prints a timestamp to inform the user when the conversion was performed.
# This is useful for record-keeping and tracking when each calculation was made.
# If you only need the timestamp once, you can remove the duplicate lines.
# This section is reserved for future enhancements or features.

#This is number 1 and 2 


