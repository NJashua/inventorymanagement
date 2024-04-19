# enter a word and it will return half of the word 
string_val = input("Enter a string")
len_ofstring = len(string_val)
result = int(len_ofstring/2)
print(string_val[0:result])