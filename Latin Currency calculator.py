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

#Now we need to convert the leftover currency to us dollarss

usd_from_cop = cop_leftover * rate_cop_to_usd
usd_from_pen = pen_leftover * rate_pen_to_usd
usd_from_brl = brl_leftover * rate_brl_to_usd
print(f'USD from COP: ${usd_from_cop:.2f}')
print(f'USD from PEN: ${usd_from_pen:.2f}')

