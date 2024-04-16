def get_full_name(first_name : str, last_name : str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

# print(get_full_name("yateesh", "chandra"))

def get_age(name : str, age : int):
    res = "I am " + name + " and I am " + str(age)
    return res

# print(get_age("Yateesh", 23))

def get_item_list(items : list[str]):
    for item in items:
        print(item)

print(get_item_list(["Yateesh", "Chandra"]))