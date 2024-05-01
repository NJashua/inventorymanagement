class person:
    def __init__(self, name, age, number) -> None:
        self.name=  name 
        self.age = age
        self.number = number
    def make_call(self):
        print("Calling to {} and number is {}".format(name, number))


name = "John"
age = 23
number = 9390779308
call_class = person(name, age, number)
call_class.make_call()