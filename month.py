import os

days = [
    list(range(1,31+1)), # January
    list(range(1,29)), # February
    list(range(1,31+1)), # March
    list(range(1,30+1)), # April
    list(range(1,31+1)), # May          
    list(range(1,30+1)), # June
    list(range(1,31+1)), # July
    list(range(1,31+1)), # August
    list(range(1,30+1)), # September
    list(range(1,31+1)), # October
    list(range(1,30+1)), # November
    list(range(1,31+1)), # December
]


YEAR = 2023

MONTH = "march".lower()

months = {
    "january": 0,
    "february": 1,
    "march": 2,
    "april": 3,
    "may": 4,
    "june": 5,
    "july": 6,
    "august": 7,
    "september": 8,
    "october": 9,
    "november": 10,
    "december": 11,
}

for day in range(1,24):
    open(f"month-py/{day}-{months[MONTH]+1}-{YEAR}-1.txt","w")
    os.system(f"git add month-py/{day}-{months[MONTH]+1}-{YEAR}-1.txt")
    os.system(f"git commit --date=\"{day}-{months[MONTH]+1}-{YEAR} 8:08:08\" -m \"month-py/{day}-{months[MONTH]+1}-{YEAR}.txt\"")

BRANCH = "main"

os.system(f"git push origin {BRANCH}")