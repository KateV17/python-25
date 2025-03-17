class Student:
    "Класс для студента"
    def __init__(self, name:str, age:int, grade:str, favorite_subject:str):
        "Индивидуально для каждого студента"
        self.name = name
        self.age = age
        self.grade = grade
        self.favorite_subject = favorite_subject
        print(f"Имя: {self.name}, " f"Возраст: {self.age}, " f"Класс: {self.grade}, " f"Любимый предмет: {self.favorite_subject}.")

    def greeting(self):
        "Привествие с учителем"
        print("Здравствуйте, Елена Леонидовна")

    def classmate(self):
        "Действие с другом"
        print("*увидел друга* Привет!")


    Tihon = Student("Тихон",7, "1Н", "Физкультура")
    Tihon.greeting()
    Tihon.classmate()

    Sanya = Student("Саня", 17, "11Н", "Математика")
    Sanya.greeting()
    Sanya.classmate()