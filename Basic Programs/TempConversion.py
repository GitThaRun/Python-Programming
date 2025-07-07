F = int(input("Enter Fahrenheit Value : "))
C = int(input("Enter Celsius value : "))

ToFahrenheit = (C * 9 / 5) + 32
ToCelsius = (F - 32) * 5 / 9

print(f"Fahrenheit To Celsius : {ToCelsius : .2f}°C")
print(f"Celsius To Fahrenheit : {ToFahrenheit : .2f}°F")