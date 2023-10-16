def ask_for_the_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("what is your name : ")
    return name_answer
    
def ask_for_the_age(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + ", what is your age : ")
        try:
            age_int = int(age_str)
        except:
            print("ERROR: age must be a number")
    return age_int

def display_person_info(name, age):
    print("Your name is " + name + ", your age is " + str(age) + " years old")
    
NB_PERSON = input("Jumlah orang : ")

list_ = []
for i in range(0, int(NB_PERSON)):
    name = ask_for_the_name()
    age = ask_for_the_age(name)
    display_person_info(name, age)
    list_.append(name)

print(list_)