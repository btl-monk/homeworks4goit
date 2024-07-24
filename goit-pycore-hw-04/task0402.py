print("_____________________________task02________________________________________________________________")

import pathlib

# path to file with all kitties
cats_info_file = pathlib.Path(__file__).parent / "data/cats.txt"

def get_cats_info(all_cats_file):
    cats = []
    
    try:
        with open(all_cats_file, "r", encoding="utf-8") as cats_list:
            for line in cats_list:
                cat = line.strip().split(',')
                print(cat)

                if len(cat) == 3:
                    cat_id = cat[0].strip()
                    cat_name = cat[1].strip()
                    cat_age = int(cat[2].strip())
                    
                    cat_info = {
                        'id': cat_id,
                        'name': cat_name,
                        'age': cat_age
                    }
                    cats.append(cat_info)
                else:
                    print(f"Incorrect format line in source data file: {line}")
    # reporting that file with kitties not exist
    except FileNotFoundError:
        print(f"File {cats_info_file} not found.")

    print(cats)
    return cats


get_cats_info(cats_info_file)