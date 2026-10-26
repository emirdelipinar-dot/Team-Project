def display_menu():
    print("Welcome to the Child Tracking Application")
    print("1. Add Child")
    print("2. View Children")
    print("3. Update Child Information")
    print("4. Delete Child")
    print("5. Exit")


def age(Date_of_Birth):
    from datetime import datetime
    birth_date = datetime.strptime(Date_of_Birth, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def sleep_hours(Sleep_Hours):
    hours, minutes = map(int, Sleep_Hours.split(':'))
    total_minutes = hours * 60 + minutes
    return total_minutes



while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        Name = input("Enter child's name: ")
        Date_of_Birth = input("Enter child's date of birth (DD-MM-YYYY): ")
        birth_time =    Date_of_Birth.split()
       
        if len(birth_time) == 3:
            day, month, year = map(int, birth_time)
            dayf = int(day)
            monthf = int(month)
            yearf = int(year)
        else:
            print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
            continue
       
        Gender = input("Enter child's gender (1 for male, 2 for female): ")
       
        Sleep_Hours = input("Enter sleep hours hh:mm: ")
        Sleep_time = Sleep_Hours.split()
       
        if len(Sleep_time) == 2:
            hours, minutes = map(int, Sleep_time)
        
            hoursf = int(hours)
            minutesf = int(minutes)
        
        else:
            print("Invalid sleep hours format. Please enter the time in hh:mm format.")
            continue
       
        Child_Age = age(Date_of_Birth)
        Sleep_Minutes = sleep_hours(Sleep_Hours)
         
        print(f"Child {Name} added successfully!")

    if choice == '2':
        print(f"Child Name: {Name}")
        print(f"Child Age: {Child_Age}")
        print(f"Child Gender: {Gender}")
        print(f"Sleep Hours: {Sleep_Hours} ({Sleep_Minutes} minutes)")