from dataclasses import dataclass
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    students_count = 0
    for group in groups:
        students_count = max(students_count, len(group.students))

    return students_count


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
    return len(students)


def read_groups_information() -> set:
    specialities = []

    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    for group in groups:
        specialities.append(group.specialty.name)

    return set(specialities)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
