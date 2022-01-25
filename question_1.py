# MEE 1/25/22

from random import randint

def clone_trooper():
    num = 0
    name_lst = []
    x = 0
    while True:
        num = randint(0, 9999)
        new_name = str.capitalize(input("Would you like a new name?"))
        if new_name == "Y":
            if num < 10:
                name = "CT-000" + str(num)
                print("Clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

            elif num < 100 and num >= 10:
                name = "CT-00" + str(num)
                print("Clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

            elif num < 1000 and num >= 100:
                name = "CT-0" + str(num)
                print("Clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

            elif num >= 1000:
                name = "CT-" + str(num)
                print("Clone trooper name: {0}".format(name))
                name_lst.insert(x, name)
                x += 1

        if new_name == "N":
            print(name_lst)
            break

clone_trooper()