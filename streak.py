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

YEAR = 2022

for month in range(12):
    for day in days[month]:
        open(f"files-py/{day}-{month+1}-{YEAR}-1.txt","w")
        os.system(f"git add files-py/{day}-{month+1}-{YEAR}-1.txt")
        os.system(f"git commit --date=\"{YEAR}-{month+1}-{day} 8:08:08\" -m \"files-py/{day}-{month+1}-{YEAR}.txt\"")

BRANCH = "main"

os.system(f"git push origin {BRANCH}")
