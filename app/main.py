from datetime import datetime
import dataclasses
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as file:
        max_students = 0
        for group in groups:
            pickle.dump(group, file)
            max_students = max(max_students, len(group.students))
    return max_students


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)
    return len(students)


def read_groups_information() -> list:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        try:
            while True:
                group = pickle.load(file)
                specialties.add(group.specialty.name)
        except EOFError:
            pass
    return list(specialties)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as file:
        try:
            while True:
                student = pickle.load(file)
                students.append(student)
        except EOFError:
            pass
    return students
