class Studentms:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__grades = {}

    def view_student(self):
        return f"name :{self.name} , Roll No : {self.roll_no} , grades : {self.__grades.keys()} , {self.__grades.values()}"

    def update_student(self, sub, marks):
        self.__grades[sub] = marks

    def calculate_avg(self):
        if not self.__grades:
            return 0
        return sum(self.__grades.values() / len(self.__grades))


class Studentmanager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if isinstance(student, Studentms):
            self.students.append(student)

    def delete_student(self, roll_no):
        for stu in self.students:
            if stu.roll_no == roll_no:
                self.students.remove(stu)
                return True

        return False

    def get_student(self, roll_no):
        for stu in self.students:
            if stu.roll_no == roll_no:
                return stu
        return None


manager = Studentmanager()

while True:
    print("\n🎓 Student Management System")
    print("1. Add Student")
    print("2. Update Grades")
    print("3. View Student")
    print("4. Calculate Average")
    print("5. Delete Student")
    print("6. List All Students")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        student = Studentms(name, roll)
        manager.add_student(student)
        print("✅ Student added.")

    elif choice == "2":
        roll = input("Enter roll number: ")
        student = manager.get_student(roll)
        if student:
            subject = input("Enter subject: ")
            marks = int(input("Enter marks: "))
            student.update_student(subject, marks)
            print("✅ Marks updated.")
        else:
            print("❌ Student not found.")

    elif choice == "3":
        roll = input("Enter roll number: ")
        student = manager.get_student(roll)
        if student:
            print(student.view_student())
        else:
            print("❌ Student not found.")

    elif choice == "4":
        roll = input("Enter roll number: ")
        student = manager.get_student(roll)
        if student:
            avg = student.calculate_avg()
            print(f"📊 Average marks: {avg:.2f}")
        else:
            print("❌ Student not found.")

    elif choice == "5":
        roll = input("Enter roll number: ")
        if manager.delete_student(roll):
            print("✅ Student deleted.")
        else:
            print("❌ Student not found.")

    elif choice == "6":
        all_students = manager.list_students()
        if all_students:
            for stu in all_students:
                print(stu)
        else:
            print("⚠️ No students found.")

    elif choice == "7":
        print("👋 Exiting program.")
        break

    else:
        print("❌ Invalid choice.")
