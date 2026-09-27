max_value = 0
min_value = float(1000)
max_country = ""
min_country = ""
max_year = int(0)
min_year = int(0) 



with open('life-expectancy.csv', 'r') as file:
  next(file)
  user_input = int(input("Enter the year of interest: "))
  for line in file:
    sections = line.split(",")
    country = sections[0]
    year = sections[2]
    life_expectancy_rate = float(sections[3])

    if life_expectancy_rate > max_value:
     max_value = life_expectancy_rate
     max_country = country
     max_year = year 
    if life_expectancy_rate < min_value:
      min_value = life_expectancy_rate
      min_country = country
      min_year = year
  print(f"The overall max life expectancy is: {max_value} from {max_country} in {max_year}")
  print(f"The overall min life expectancy is: {min_value} from {min_country} in {min_year}")







