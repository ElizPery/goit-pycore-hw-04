from pathlib import Path

def get_cats_info(path: str) -> list[dict]:
    # Function takes path to the file with data about cats (in line format: <id>,<name>,<age>) and return list of dict with keys: id, name, age; and values respectively

    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_data = file.readlines()

            cats_data_splited = [cat.strip().split(',') for cat in cats_data]
            cats_list_of_dict = [{'id': id, 'name': name, 'age': age} for id, name, age in cats_data_splited]

            return cats_list_of_dict
    except:
        print('Data have lost or inaccurate, please try again and check data file')


get_cats_info(Path(__file__).parent / 'cats.txt')