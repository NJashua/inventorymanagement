word = input()
n = int(input())
length = len(word)
half_length = length - 3
slice_word = word[half_length:]
part = slice_word * n 
print("repeated word is: ", part)

# adding some complex

word = input()
n = int(input())
print(word + (' ' + word) * (n-1))

# star repetition on middle of the word

word = input("Enter word: ")
first_two = word[:2]
last_two = word[-2:]
middle = "*" * (len(word) - 4)
print(first_two + middle + last_two)
