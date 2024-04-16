class Person :
    def __init__(self, name : str = None):
        self.name = name
    
def get_person_name(one_person : Person):
    return one_person.name

person= Person("Yateesh")
person1 = Person()
print(get_person_name(person1))