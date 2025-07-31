# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def speak(self):
#         print("some food")


# class Dog(Animal):

#     def __init__(self, name, breed):
#         super().__init__("dog")
#         self.name = name
#         self.breed = breed

#     def speak(self):
#         print(f"{self.name} says Woof!")


# obj1 = Dog("tom", "somebreed")
# print(obj1.speak())


# class Person:
#     def __init__(self):
#         pass

# class Person:
#     def __init__(self, name):
#         self.name = name          # public
#         self._age = 30            # protected (just a warning)
#         self.__salary = 50000     # private (name mangled)

#     def show(self):
#         print(self.name, self._age, self.__salary)

# p = Person("Raj")
# p.show()

# print(p.name)       # ✅ OK
# print(p._age)       # ⚠️ OK, but shouldn't be touched
# print(p.__salary)   # ❌ Error


class Student:
    school_name = "Future Academy"

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = {}

    def add_marks(self, subject, marks):
        self.__marks[subject] = marks

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def is_calid_roll(roll):
        return isinstance(roll, int) and roll > 0


stObj1 = Student(name="someName", roll_no=65)
# print(stObj1.__dict__)
# print(stObj1.school_name)
stObj1.add_marks(subject="maths", marks=99)
# print(stObj1.__dict__)
# print(stObj1.get_marks())
