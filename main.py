import os

# Create tons of files.

NUMBER_OF_COMMITS = 3500

for i in range(1500,NUMBER_OF_COMMITS):
    open(f"./files/{i}.txt", "w")
    os.system(f"git add ./files/{i}.txt")
    os.system(f'git commit -m "{i}.txt"')

os.system("git push origin main")