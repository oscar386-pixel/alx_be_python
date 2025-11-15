#weather_advice.py

#prompt user for current weather
weather = input("whats the weather like today? (suuny/rainy/cold):")

if weather == "suuny":
  print("Wear a t-shirt and sunglasses")
elif weather == "rainy":
  print("Don't your umbrella and a raincoat.")
elif weather == "cold":
  print(" Make sure to wear a warm coat and a scarf.") 
else:
  print("Sorry, i dont have recommendation for this weather.")   