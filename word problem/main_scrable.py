import scrable

letters = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"


def check_for_never_used_double(letter):
    """
    CHECKS FOR A LETTER WHICH IS NEVER USED DOUBLE IN SCRABBLE / ENGLISH

    :param letter:
    :return: Bool
    """
    for word in scrable.words_dic:
        if letter + letter in word:
            return True
    return False


def check_for_double_letters(word):
    """
    Checks for double letters used in scrabble / english eg: "aa"
    :param word:
    :return: bool
    """
    for letter in letters:
        if letter + letter in word:
            return True
    return False


# CHECK FOR THOSE WORDS WHICH HAVE ALL THE VOWELS IN IT.
def has_all_vowels(word):
    """
    Checks for those words which have all the vowels in it. eg: "warehousing"
    :param word:
    :return: bool
    """
    for letter in vowels:
        if letter not in word:
            return False

    return True


for word in scrable.words_dic:
    if has_all_vowels(word):
        print("Has all the vowels: " + word)
        f = open("kkk.txt", "a+")
        f.write(word + "\n")
        f.close()

    if check_for_double_letters(word):
        print("Has a double letters in it: " + word)

# TO PRINT THOSE LETTERS WHICH ARE NEVER USED IN ENGLISH DOUBLE LIKE "AA"
for letter in letters:
    if not check_for_never_used_double(letter):
        print(letter + " Never appeared double")





"""
v = "aeiou"
strings = ["warehousing","pineapple","apple","irfan","ppp","k","rr"]
counter = 0

def abcc(word):
    for letter  in v:
        if letter not in word:
            return False
    return True

for name in strings:
    if abcc(name):
        counter += 1
        print(str(counter) + ": "+name)

#--------------------------------------------------------------------------#
#------------SAME FUNCTIONALITY AS THE ABOVE FUNCTION DOES WITH IF---------#
for name in strings:


    if v[0] in name:
        if v[1] in name:
            if v[2] in name:
                if v[3] in name:
                    if v[4] in name:
                        counter += 1
                        print(counter,": " +name)


"""
