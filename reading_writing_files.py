# FILE MODES R FOR READING W FOR WRITING
f = open("capitals.txt", 'r')
capitals = []
for line in f:
    line = line.strip()
    capitals.append(line)
    print(line)

f.close()

d = open("new.txt", "w")

for c in capitals:
    d.write(c + "\n")

d.close()

# IF YOU OPEN FILE WITH (WITH OPEN) THEN NO NEED TO CLOSE
# THE FILE IT WILL AUTOMATICALLY CLOSE THE FILE ONCE YOU ARE DONE.

with open("user.txt", "w") as usr:
    for x in range(5):
        a = input("Enter your name plz: ")
        b = input("Enter your roll num plz: ")
        usr.write(a + ': ' + b + '\n')

# PRINTING MATH'S TABLE AND THEN SAVING INTO TEXT FILE

usr_input = int(input("How Many Tables do you want to print & save? "))
with open("Table.txt", "w") as tb:
    tb.write("Tables from 1 to " + str(usr_input) + "\n")
    tb.write("---------------" + "\n")

    for x in range(1, usr_input + 1):
        print("---------------")
        for y in range(1, 11):
            print(str(x) + " x " + str(y) + " = ", x * y)
            tb.write(str(x) + " x " + str(y) + " = " + str(x * y) + "\n")
        print("---------------")
        tb.write("---------------" + "\n")
