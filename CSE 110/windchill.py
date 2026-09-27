def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32
def wind_chill(temperature,wind_speed):
  return 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)



temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").upper()


if unit == 'C':
        temperature = celsius_to_fahrenheit(temperature)
        print(f"Converted temperature to {temperature}F.")
print(f"At temperature {temperature:.1f}F:")


for wind_speed in range(5, 65, 5):
  wind_chill_result = wind_chill(temperature, wind_speed)
  print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill_result:.2f}F")

