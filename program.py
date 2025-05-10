#! /bin/python3
import json 
from datetime import date

### SETUP  
try: 
    with open('profile.json', 'r') as f:
        print("📂 profile.json found\n")
        user_profile = json.load(f)

except FileNotFoundError:
    print("📂 profile.json not found\n")

    # Questionare: - habit and why?  
    print("|-=-{ 📜 PROGRAM SETUP 🔧 }-=-")
    print("|")
    print("| 🎯 What daily habit would you like to form?")

    while True: 
        reminder_habit = input("| 💬 I want to... ") 
        if reminder_habit != "":
            break
    while True: 
        reminder_reason = input("| 💬 Because... ")
        if reminder_reason != "":
            break

    # Collect todays date, update startup checker  
    started = date.today()

    # Construct data object user_profile
    user_profile = {
            "reminder_habit": reminder_habit,
            "reminder_reason": reminder_reason,
            "started_year": started.year, 
            "started_month": started.month, 
            "started_day": started.day, 
            }
    
    # Store user_profile in json 
    with open('profile.json', 'w') as f:
       json.dump(user_profile, f)
   
    # Finishing message   
    print("|")
    print("| ✅ => Setup completed...")
    print("| 🚀 => Launch again to check progress...")
    print("|")

    # Quit Program 
    exit()

### RANK GETTER 
def rank_getter(number): 
    # Caclulate rank based on days, show days until rankup 
    if number < 7: 
        print("| 🏅 Rank: Slime -", 7 - number, "days until rankup") 
    elif number < 14: 
        print("| 🏅 Rank: Squire -", 14 - number, "days until rankup") 
    elif number < 21: 
        print("| 🏅 Rank: Adept -", 21 - number, "days until rankup") 
    elif number < 31: 
        print("| 🏅 Rank: Apprentice -", 31 - number, "days until rankup") 
    elif number < 90: 
        print("| 🏅 Rank: Knight -", 90 - number, "days until rankup") 
    elif number < 180: 
        print("| 🏅 Rank: Champion -", 180 - number, "days until rankup") 
    elif number < 365: 
        print("| 🏅 Rank: Master -", 365 - number, "days until rankup") 
    elif number < 900: 
        print("| 🏅 Rank: Hero -", 1825 - number, "days until rankup") 
    elif number < 1825: 
        print("| 🏅 Rank: Mythic -", 3650 - number, "days until rankup") 
    elif number >= 1825: 
        print("| 🏅 Rank: Ascendant - You've reached the highest rank!")

### PROGRAM START 
def main(): 
    # Collect and calculate date 
    date_started = date(user_profile["started_year"],
                        user_profile["started_month"],
                        user_profile["started_day"]) 
    today = date.today()
    delta = today - date_started

    # Print status 
    print("|-=-{ 🧙 HABIT JOURNAL 🐉 }-=-")
    print("|")
    print("| 🎯 Quest:", user_profile["reminder_habit"].capitalize()) 
    print("| 📅 Day:", str(delta.days))
    rank_getter(delta.days) 
    print("| 🧠 Reason:", "Because", user_profile["reminder_reason"] + '.')
    print("|") 

if __name__ == "__main__":
    main()

