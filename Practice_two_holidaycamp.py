#Practice 2 - School Holiday Camp Program

# LIST OF CAMPS
camps = {
    1: {"name": "Cultural Immersion", "days": 5, "cost": 800},
    2: {"name": "Kayaking and Pancakes", "days": 3, "cost": 400},
    3: {"name": "Mountain Biking", "days": 4, "cost": 900}
}


# List of FUNCTIONS
def get_username():
    nametry = True
    while nametry == True:
        letter_only = True
        username_input = input("Please enter your name: ").title()
        for char in username_input:
            if not char.isalpha():
                letter_only = False

        if letter_only == False:
            print("Letters only. Please try again!")
        elif username_input == "":
            print("Please input your name.")
        else:
            nametry = False
            print(f"Hello {username_input}!")
            return username_input
            
get_username()
