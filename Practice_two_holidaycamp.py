#Practice 2 - School Holiday Camp Program

# LIST OF CAMPS
camps = [
    {"name": "Cultural Immersion", "days": 5, "cost": 800},
    {"name": "Kayaking and Pancakes", "days": 3, "cost": 400},
    {"name": "Mountain Biking", "days": 4, "cost": 900}
]

mealsop = {"Standard", "Vegetarian", "Vegan"}


# List of FUNCTIONS
def get_username():
    #Enables a while loop
    nametry = True
    while nametry == True:
        #While this function is TRUE, it will ask for the user's name.
        letter_only = True
        username_input = input("Please enter your name: ").strip().title()
        for char in username_input:
            #If ONE of the characters is not a letter, this is set to false.
            if not char.isalpha():
                letter_only = False

        if letter_only == False:
            print("Letters only. Please try again!")
        elif username_input == "":
            print("Please input your name.")
        else:
            nametry = False
            print(f"{username_input}")
            return username_input


def get_age():
    #Loops the code if 'agetry' remains TRUE.
    agetry = True
    while agetry == True:
        number_only = True
        age_input = input("Please enter your age: ")
        for dig in age_input:
            if not dig.isdigit():
                number_only = False

        if number_only == False:
            agetry = False
            print("Invalid! Stopping.")
            print("Invalid! Stopping..")
            print("Invalid! Stopping...")
            return False
        elif age_input == "":
            print("Enter your age.")
        elif int(age_input) < 5 or int(age_input) > 17:
            agetry = False
            print("The camp is only for people between the age of 5-17.")
            return False
        else:
            agetry = False
            return int(age_input)
            
def camp_options():
    for index, camp in enumerate(camps, start=1):
        print(f"{index}. {camp['name']} - This is for {camp['days']} days and costs ${camp['cost']}.")

    camp_pickwhile = True
    while camp_pickwhile == True:
        camp_pick = input("Enter the number of the camp you want: ")
        if camp_pick == "":
            print("Please enter a number: ")
        elif int(camp_pick) > len(camps):
            print("Please pick from the options above: ")
        else:
            camp_pickwhile = False
            print(f"{camp_pick}")
            return camp_pick

def shuttle():
    shuttleconfirm = input("Do you want to take the shuttle buys? Enter Yes or No: ").strip().title()
    if shuttleconfirm == "True":
        return True
    elif shuttleconfirm == "False":
        return False

def get_meal():
    mealask = True
    while mealask == True:
            print("There are three meal options!")
            for meal in mealsop:
                print(f"{meal}")

            user_finmeal = input("Choose the meal option: ").strip().title()
            if user_finmeal in mealsop:
                mealask = False
                print(f"{user_finmeal}")
                return user_finmeal
            else:
                print("Please pick from the meals above.")

def calculate_cost(camp_choice, transport):
    if shuttle == True:
        total_cost = {camp_choice['cost']} + 80
    else:
        total_cost = {camp_choice['cost']}

#MAIN --------------------------------------------------------------------------------------

print()

repeat = True
while repeat:
    print("Welcome to Tane's Holiday Camps Registration!")

    name = get_username()
    age = get_age()

    camp_choice = camp_options()
    transport = shuttle()
    meal_choice = get_meal()

    total_cost = calculate_cost(camp_choice, transport)

    print(f"{name} (age {age}) is attending the {camp_choice} for {camp_choice['days']}.")
    print(f"They chose a {meal_choice}. The total cost is {total_cost}.")
