# MEE 1/25/22

acc = input("What is the ships acceleration? ")
tos = input("What is the ships take off speed? ")

min_runway = (float(tos) ** 2)/(float(acc) * 2)

print("The minimum runway length for this ship is {}m.".format(min_runway))