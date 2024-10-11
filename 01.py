from pathlib import Path

def total_salary(path: str) -> tuple[int]:
    # Function takes path to the file with data about developers salaries (in line format: <name>,<salary>) and return total_salary and agerage_salary (tuple of integer)

    try:
        with open(path, 'r', encoding='utf-8') as file:
            dev_data = file.readlines()
            dev_salaries = [int(dev.strip().split(',')[1]) for dev in dev_data]

            total_salary_value = sum(dev_salaries)
            average_salary = int(total_salary_value/len(dev_salaries))

            return (total_salary_value, average_salary)
    except:
        print('Data have lost or inaccurate, please try again and check data file')


total_salary(Path(__file__).parent / 'salaries.txt')