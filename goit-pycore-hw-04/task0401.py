print("_____________________________task01________________________________________________________________")
from pathlib import Path

# path to salary file
# path_to_salary_file = Path("data/salary_file.txt")
path_to_salary_file = Path(__file__).parent / "data/salary_file.txt"

try:
    path_to_salary_file.write_text('Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,6000', encoding="utf-8")
except FileNotFoundError:
        print(f"File {path_to_salary_file} not found.")

# function which calculate total and average salary
def total_salary(path):
    total = 0
    average = 0
    number_of_devs = 0
    try:
        with open(path, 'r', encoding='utf-8') as salary_file:
            for line in salary_file:
                number_of_devs += 1
                clean_string = line.strip().split(',')
                total += int(clean_string[1])
        
        average = int(total/number_of_devs)

        return total, average
    except FileNotFoundError:
        print(f"File {path_to_salary_file} not found.")
        return total, average
    
#   display total mount salaries and average salary
if path_to_salary_file.exists():
    total, average = total_salary(path_to_salary_file)
    print(f"Total mount of salaries: {total}, Avarage salary: {average}")