# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed


# obj1 = Dog("someDog", "someBreed")

# # obj1.name = "sfd"
# # obj1.__dict__["name"] = 'fvfedd'
# obj1.__dict__["price"] = 455
# print(obj1.name)
# print(obj1.__dict__)


class SomeClass:
    pincode = 58545

    def __init__(self, name, num):

        self.name = name
        self.num = num
        self.pinnum = self.pincode


obj1 = SomeClass("someName", 434)
# print(obj1.__dict__)
# print(obj1.pinnum)
# print(obj1.pincode)

obj1.pincode = 12345
print(SomeClass.pincode)
print(obj1.pincode)



