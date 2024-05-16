"""
def get_list(list_values):
    current = list_values
    while current:
        print(current.val, end="")
        current = current.next
    print(None)

def remove_duplacates(list_a):
    current = list_a

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return current

list_a = get_list(input("Enter your list numbers: "))

print(remove_duplacates(list_a)) """


def get_uniquelist(list_a):
    empty_list = []
    for item in list_a:
        if item not in empty_list:
            empty_list.append(item)
    return empty_list

list_a= input("Enter a list: ")
print(get_uniquelist(list_a))