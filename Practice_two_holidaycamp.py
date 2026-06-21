#Practice 2 - School Holiday Camp Program

# LIST OF CAMPS
camps = {
    1: {"name": "Cultural Immersion", "days": 5, "cost": 800},
    2: {"name": "Kayaking and Pancakes", "days": 3, "cost": 400},
    3: {"name": "Mountain Biking", "days": 4, "cost": 900}
}


# List of FUNCTIONS
def get_username():
    #Enables a while loop
    nametry = True
    while nametry == True:
        #While this function is TRUE, it will ask for the user's name.
        letter_only = True
        username_input = input("Please enter your name: ").title()
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
            return True


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
            return True
            
def camp_options():
    camp_number = 0
    for index, camp in enumerate(camps, start=1):
        print(f"{index}. {camp['name']} - This is for {camp['days']} days and costs ${camp['cost']}.") 

    camp_pick = input("Enter the camp you want: ")
    
        
print("Welcome to Tane's Holiday Camps Registration!")
get_username()
get_age()
camp_options()
