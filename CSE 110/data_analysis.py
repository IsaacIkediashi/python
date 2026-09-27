
max_life = 0
min_life = 1000
max_country = ""
max_year = 0
min_country = ""
min_year = 0


print("Life Expectancy Analysis")
year = input("Enter the year of interest: ")
country = input("Enter the country of interest: ")


year_max = 0
year_min = 1000
year_total = 0
year_count = 0
country_max = 0
country_min = 1000
country_total = 0
country_count = 0


with open('life-expectancy.csv') as file:
    # I researched code to skip the first line in the csv file i.e Skip header
    next(file)
    
    
    for line in file:
        parts = line.strip().split(",")
        current_country = parts[0]
        current_year = parts[2]
        life = float(parts[3])
        
        # Overall max/min
        if life > max_life:
            max_life = life
            max_country = current_country
            max_year = current_year
        if life < min_life:
            min_life = life 
            min_country = current_country
            min_year = current_year
            
        # Year-specific stats
        if current_year == year:
            year_total += life
            year_count += 1
            if life > year_max:
                year_max = life
            if life < year_min:
                year_min = life
                
        # Country-specific stats
        if current_country.lower() == country.lower():
            country_total += life
            country_count += 1
            if life > country_max:
                country_max = life
            if life < country_min:
                country_min = life


print("\nOverall Statistics:")
print(f"Max Life Expectancy: {max_life:.2f} in {max_country} ({max_year})")
print(f"Min Life Expectancy: {min_life:.2f} in {min_country} ({min_year})")

if year_count > 0:
    print(f"\nFor the year {year}:")
    print(f"Average Life Expectancy: {year_total/year_count:.2f}")
    print(f"Max Life Expectancy: {year_max:.2f}")
    print(f"Min Life Expectancy: {year_min:.2f}")
else:
    print(f"\nNo data found for year {year}")

if country_count > 0:
    print(f"\nFor {country}:")
    print(f"Average Life Expectancy: {country_total/country_count:.2f}")
    print(f"Max Life Expectancy: {country_max:.2f}")
    print(f"Min Life Expectancy: {country_min:.2f}")
else:
    print(f"\nNo data found for country {country}")
