import requests

API = 'YOUR_API_KEY'

fromCurr = input("Enter from which : ")
toCurr = input("Enter to which : ")
amount = int(input("Enter amount : "))

response = requests.get(f'https://www.amdoren.com/api/currency.php?api_key={API}&from={fromCurr}&to={toCurr}&amount={amount}')

if response.json()['error'] == 0:
  print(f"{amount} {fromCurr} = {response.json()['amount']} {toCurr}")
else:
  print(f"We found {response.json()['error']} errors.")
  print(f"{response.json()['error_message']}")