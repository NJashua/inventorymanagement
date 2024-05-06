char = input("Enter a character: ")

if char.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(char, "is a vowel")
else:
    print(char,"is a consonant")