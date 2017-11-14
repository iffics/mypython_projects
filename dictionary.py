""" DICTIONARIES  are unordered bags of key-value pairs.
    ITS KEY, VALUE PAIRS JUST LIKE HASHMAPS
    ! KEYS HAVE TO BE UNIQUE WHERE AS VALUES DON'T MATTER

"""
students = {1: 'irfan', 2: 'khan', 3: 'kakar', 4: 'ajmal', 5: 'anwar', 6: 'riaz'}

print(len(students))

# LETS PRINT BOTH KEY AND VALUE PAIRS

print('--------')
for x, y in students.items():
    print(x, y)

print('--------')

# one way
for s in range(1, len(students) + 1):
    print(students[s])
print('--------')

# to print the keys
for ss in students:
    print(ss)

for ss in students.keys():
    print(ss)
print('--------')

# to print the values
for ss in students.values():
    print(ss)

# LETS ADD A NEW STUDENT RECORD TO THE STUDENTS DIC

students[7] = 'ikk'

print(students)

# LETS TAKE INPUT FROM USER AND ADD INTO DICTIONARY:

counter = 0
while counter < 5:

    a = input("Enter the key plz: ")
    if int(a) in students.keys():
        print("Sorry the key is already been used: ")
        continue
    students[a] = input("Enter the Value plz: ")
    print(students[a])
    counter += 1
