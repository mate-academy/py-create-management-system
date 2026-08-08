import pickle
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    # Повертаємо кількість студентів
    return len(students)


def read_groups_information() -> set:
    specialty_name = set()

    try:
        with open("groups.pickle", "rb") as file:
            while True:
                try:
                    read_groups = pickle.load(file)
                    for group in read_groups:
                        specialty_name.add(group.specialty.name)
                except EOFError:
                    break
    except FileExistsError:
        print("File 'groups.pickle' not found.")

    return specialty_name


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        list_students = pickle.load(file)
    return list_students


# Приклад створення спеціальності
specialty = Specialty("manager", 101)

# Приклад створення студентів
student1 = Student(
    "Іван",
    "Іванов",
    datetime(2005, 6, 15),
    90.5,
    True,
    "+380501234567",
    "Київ, вул. Незалежності, 10"
)

student2 = Student(
    "Марія",
    "Петренко",
    datetime(2004, 12, 20),
    85.0,
    False,
    "+380501234568",
    "Львів, вул. Січових Стрільців, 5"
)

student3 = Student(
    "Олександр",
    "Коваль",
    datetime(2003, 8, 25),
    78.0,
    True,
    "+380501234569",
    "Одеса, вул. Дерибасівська, 12"
)
student4 = Student(
    "Sanya",
    "Ivanov",
    datetime(2001, 1, 2),
    10.5,
    True,
    "355355",
    "Odessa"
)
group_1 = Group(specialty, 2, [student1])
group_2 = Group(specialty, 3, [student2, student3, student4])

group_all = [group_1, group_2]
maximum_students = write_groups_information(group_all)
print(maximum_students)  # 3

all_students = [student1, student2, student3, student4]
inf_students = write_students_information(all_students)
print(inf_students)  # 4

# Приклад виводу унікальних назв спеціальностей:
specialties = read_groups_information()
print(specialties)  # {'manager'}

# Приклад виводу списку студентів:
all_list_stidents = read_students_information()
print(all_list_stidents)
