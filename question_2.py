# MEE 1/25/22

v1 =input("What is the initial velocity? ")
v2 = input("what is the final velocity? ")
time = input("What is the total time it takes? ")

v = int(v2) - int(v1)

acceleration = v / int(time)

print("The average acceleration is {0} m/s/s".format(v))