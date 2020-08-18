students = [ "Jolene", "Izzy", "Susan", "Boudreaux", "Thibodeaux", "Dennis", "Dee"]
file = open("output_file.txt", "w")
file.write("Here is a list of names: \n")

for s in students:
    file.write(s + "\n")

file.close()
