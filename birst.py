from collections import defaultdict
from datetime import datetime, timedelta





def get_birthdays_per_week(users):
    birthdays_by_day = defaultdict(list)

  
    today = datetime.today().date()

    print(today)
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days<=7 and delta_days>0:
            birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")  
            if delta_days==2:
                delta_days=delta_days+1
                birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A") 
            elif delta_days==1:
                delta_days=delta_days+2
                birthday_weekday = (today + timedelta(days=delta_days)).strftime("%A")
        else:
            continue
 
        birthdays_by_day[birthday_weekday].append(name)

    for day, names in birthdays_by_day.items():
        print(f"{day}: {', '.join(names)}")

    names.i



users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 12, 5)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 12, 7)},
    {"name": "Mark Zuckerberg", "birthday": datetime(1984, 5, 14)},
    {"name": "Mark Zuckerbergf", "birthday": datetime(1984, 12, 3)},
    {"name": "Steve Jobs1", "birthday": datetime(1955, 12, 2)},
]        

print(get_birthdays_per_week(users))
