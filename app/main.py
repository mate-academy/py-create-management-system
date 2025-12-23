import dataclasses
from datetime import datetime
import pickle
import os


# Класс Specialty
@dataclasses.dataclass
class Specialty:
    name: str
    number: int


# Класс Student
@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


# Класс Group
@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


# Функция для записи информации о группах
def write_groups_information(groups: list[Group]) -> int:
    if not groups:  # Если список групп пуст
        return 0
    max_students = max(len(group.students) for group in groups)
    with open("groups.pickle", "wb") as file:  # Файл в текущей директории
        pickle.dump(groups, file)
    return max_students


# Функция для записи информации о студентах
def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:  # Файл в текущей директории
        pickle.dump(students, file)
    return len(students)


# Функция для чтения информации о группах
def read_groups_information() -> list[str]:
    if not os.path.exists("groups.pickle"):  # Проверяем, существует ли файл
        return []  # Возвращаем пустой список, если файла нет
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
    specialties = set(group.specialty.name for group in groups)
    return list(specialties)


# Функция для чтения информации о студентах
def read_students_information() -> list[Student]:
    if not os.path.exists("students.pickle"):  # Проверяем, существует ли файл
        return []  # Возвращаем пустой список, если файла нет
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students


# Пример использования
if __name__ == "__main__":
    # Создание специальности
    specialty = Specialty(name="Computer Science", number=101)

    # Создание студентов
    student1 = Student(
        first_name="John",
        last_name="Doe",
        birth_date=datetime(2000, 1, 1),
        average_mark=4.5,
        has_scholarship=True,
        phone_number="1234567890",
        address="123 Main St"
    )
    student2 = Student(
        first_name="Jane",
        last_name="Smith",
        birth_date=datetime(2001, 2, 2),
        average_mark=4.7,
        has_scholarship=False,
        phone_number="0987654321",
        address="456 Elm St"
    )

    # Создание группы
    group = Group(
        specialty=specialty,
        course=1,
        students=[student1, student2]
    )

    # Запись информации о группах
    max_students = write_groups_information([group])
    print(f"Max students in a group: {max_students}")

    # Запись информации о студентах
    num_students = write_students_information([student1, student2])
    print(f"Number of students: {num_students}")

    # Чтение информации о группах
    specialties = read_groups_information()
    print(f"Specialties: {specialties}")

    # Чтение информации о студентах
    students = read_students_information()
    for student in students:
        print(f"Student: {student.first_name} {student.last_name}")
