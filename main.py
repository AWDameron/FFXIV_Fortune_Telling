import Fortune_Lists
import random
import os

def text_file_generator(file_name):
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Create the absolute file path
    file_path = os.path.join(current_directory, file_name)
    
    # Create the file if it doesn't exist
    if not os.path.isfile(file_path):
        with open(file_path, "w") as file:
            # Just create an empty file; you could also write a header or initial content if desired
            pass
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")
    
    return file_path


def fortune_telling_random(file_path):
    #organize the major arcana into a list so we can randomly choose from it, or let the user "draw a card"
    major_arcana = ["The Ewer","The Arrow","The Bole","The Spire","The Balance","The Spear"]
    arcana_dict = {"The Ewer":Fortune_Lists.wealth_fortunes,
                   "The Arrow":Fortune_Lists.adventure_fortunes,
                   "The Bole":Fortune_Lists.love_fortunes,
                   "The Spire":Fortune_Lists.family_fortunes,
                   "The Balance": Fortune_Lists.self_fortunes,
                   "The Spear": Fortune_Lists.job_fortunes
                   }
    
    #We're using some of our variables to help create a log of the fortunes told, this way we can repeat them if needed, and for our own fun.
    #Also a good way for us to go through and change/remove fortunes that are kind of weak sauce.
    user_name = input("What is the users name(and server/or traveler i guess)")
    user_choice = int(input("Yessss, i've entered the astral plane mentally, now tell me which card do you pick? (1 thru 6 or /roll 6)"))
    random.shuffle(major_arcana)
    #print to verify code
    print(major_arcana)
    user_choice = major_arcana[user_choice-1]
    print(user_choice)
    card_direction = random.choices(["right-side up","upside-down"],weights=[55,45],k=1)[0]
    #print to verify code
    print(card_direction)
    print(f"Ah, i see in the stars that the star sign {user_choice} and I place it now before you {card_direction}")
    # Checks card direction to determine the outcome.
    if card_direction == "right-side up":
        outcome = random.choice(arcana_dict[user_choice][0])

    else:
        outcome = random.choice(arcana_dict[user_choice][1] + arcana_dict[user_choice][2])
        
    #logs the fortune into a file, does not create a new file so make sure you have the file on your computer already.
    with open(file_path, "a") as file:
        file.write(f"{user_name} drew the {card_direction} {user_choice} and received this fortune: {outcome}\n")
    
    print(f"Ah, i see it clearly now, i have my mind in sync with {user_choice} and can peer into the future")
    print(outcome)


file_path = text_file_generator("Fortunes_told.txt")
x=0
while x != "q": 
    fortune_telling_random(file_path)
    x = input("input 'q' to quit, or press enter to continue")

