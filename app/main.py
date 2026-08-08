import dataclasses
from datetime import datetime
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_students = 0
    with open("groups.pickle", "wb") as groups_pickle_file:
        for group in groups:
            pickle.dump(group, groups_pickle_file)
            max_students = max(max_students, len(group.students))

    return max_students


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as students_pickle:
        for student in students:
            pickle.dump(student, students_pickle)
    return len(students)


def read_groups_information() -> set:
    try:
        with open("groups.pickle", "rb") as groups_pickle:
            groups = set()
            while True:
                try:
                    group = pickle.load(groups_pickle)
                    groups.add(group.specialty.name)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found")
    return groups


def read_students_information() -> list[Student]:
    students = []
    try:
        with open("students.pickle", "rb") as students_pickle:
            while True:
                try:
                    student = pickle.load(students_pickle)
                    students.append(student)
                except EOFError:
                    break
    except FileNotFoundError:
        print("File not found")
    return students
