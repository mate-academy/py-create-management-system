from dataclasses import dataclass
from datetime import date
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


# 2. Функції запису даних за допомогою pickle
def write_groups_information(groups: list[Group]) -> int:
    """Записує список груп у файл groups.pickle та повертає макс.

    кількість студентів у групі.
    """
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    """Записує список студентів у файл students.pickle та повертає їхню

    кількість.
    """
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


# 3. Функції читання даних за допомогою pickle
def read_groups_information() -> set[str]:
    """Читає groups.pickle та повертає унікальні назви спеціальностей."""
    with open("groups.pickle", "rb") as file:
        groups: list[Group] = pickle.load(file)

    return {group.specialty.name for group in groups}


def read_students_information() -> list[Student]:
    """Читає students.pickle та повертає список усіх студентів."""
    with open("students.pickle", "rb") as file:
        students: list[Student] = pickle.load(file)

    return students
