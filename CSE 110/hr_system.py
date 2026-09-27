# Open the HR system file
with open('hr_system.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:
        # Strip leading/trailing whitespace and split the line into parts
        parts = line.strip().split()

        # Extract name, ID number, job title, and salary
        name = parts[0]
        id_number = parts[1]
        job_title = parts[2]
        salary = float(parts[3])  # Convert salary to float

        # Display name and job title
        print(f"Name: {name}, Title: {job_title}")

        # Display the full details (name, ID number, job title, and salary)
        print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")
        
        # Calculate the paycheck (assuming salary is annual and employee is paid twice a month)
        paycheck = salary / 24  # 24 pay periods in a year (twice a month)
        
        # If the job title is "Engineer", add a $1000 bonus to the paycheck
        if job_title == 'Engineer':
            paycheck += 1000  # Engineers get an extra $1000

        # Display the paycheck
        print(f"Paycheck for {name}: ${paycheck:.2f}")
        print()  # Newline for better readability
