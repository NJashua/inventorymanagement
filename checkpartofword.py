word = input("enter word: ")
check_word = input("enter check word: ")
value = int(input("enter start index val: "))

start_index = int(len(check_word))
end_index = start_index + value
result = word[start_index:end_index]
if check_word == result:
    print(f"the word '{check_word}' in '{word}'")
else:
    print("word not found")
