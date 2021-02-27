import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

print(format_currency(5000, "KRW"))


url = "https://www.iban.com/currency-codes"

r=requests.get(url)
iban_all=BeautifulSoup(r.text,"html.parser")

table=iban_all.find("table",{"class":"table table-bordered downloads tablesorter"})

tbody=table.find("tbody")

country_list=tbody.find_all("tr")


index_country={"index":[],"country":[],"currency code":[]}
for index,n in enumerate(country_list):
  country_name=n.find("td").string
  currency_code_name=n.find("td").find_next("td").find_next("td").string
  index_country["index"].append(index)
  index_country["country"].append(country_name)
  index_country["currency code"].append(currency_code_name)
  print(f"#{index}",country_name)

def while_function():
  true_false=True
  while true_false:
    try:
      input_number=int(input())
    except ValueError:
      print("That wasn't a number.")
    else:
      if input_number in index_country["index"]:
        country=index_country["country"][input_number]
        print(f"{country}")
        return input_number
        true_false=False
      else:
        print("Choose a number from the list.")
        


print("\n"+"Where are you from? Choose a country by number.")
input_number_1=while_function()
print("\n"+"Now choose another country.")
input_number_2=while_function()

print(index_country["currency code"][input_number_1])
currency_code_1 = index_country["currency code"][input_number_1]
currency_code_2 = index_country["currency code"][input_number_2]

print("\n"+f"How many {currency_code_1} do you want to convert to {currency_code_2}?")
how_many=float(input())


URL=f"https://transferwise.com/gb/currency-converter/{currency_code_1.lower()}-to-{currency_code_2.lower()}-rate?amount=50"

def calculate():
  a=requests.get(URL)
  transferwise=BeautifulSoup(a.text,"html.parser")
  text_success=transferwise.find("span",{"class":"text-success"}).string
  converted=how_many*float(text_success)
  home=format_currency(how_many,currency_code_1)
  another=format_currency(converted,currency_code_2)
  print(f"{home} is {another}")

try:
  calculate()
except:
  print("Not valid currency code.")
  """KPW is not valid currency code."""