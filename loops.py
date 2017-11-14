names = ['iffi', 'irfan', 'ikk', 'ikram', 'zarak', 'riaz', 'ajmal', 'anwar']
# FOR LOOP
for name in names:
    print("hello " + name)

# slightly different version
for x in range(0, len(names)):
    print(names[x])
print('---------')

# WHILE LOOP

counter = 0
print('While loop: ')
while counter < len(names):
    print(names[counter])
    counter += 1

# PRINT THE NAMES WHICH STARTS WITH VOWEL

for name in names:
    if name[0] in "AEIOU" or name[0] in "aeiou":
        print(name + " starts with vowel")

# PRINTS THE NAMES WHICH ENDS ON VOWEL

for name in names:
    if name[-1] in "AEIOU" or name[-1] in "aeiou":
        print(name + " Ends with vowel")

# PRINTS THE NAMES WHICH STARTS AND ENDS ON VOWEL

for name in names:
    if name[0] in "aeiou" and name[-1] in "aeiou":
        print(name + " Starts and Ends with vowel")
