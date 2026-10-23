import dataclasses
import pickle
from datetime import datetime


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


student_1 = Student(
    "Alex",
    "Smith",
    datetime(2005, 10, 15),
    89.5,
    True,
    "+380501234567",
    "Kyiv"
)

student_2 = Student(
    "Bob",
    "Moth",
    datetime(2004, 11, 17),
    89.7,
    True,
    "+380501277777",
    "Kyiv"
)

student_3 = Student(
    "Simon",
    "Brown",
    datetime(2006, 5, 20),
    92.5,
    True,
    "+380501111111",
    "Kyiv"
)


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int :
    with open("groups.pickle", "wb") as file:
        for group in groups:
            pickle.dump(group, file)

    result = 0
    for group in groups:
        students_count = len(group.students)

        if students_count > result:
            result = students_count

    return result


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        for student in students:
            pickle.dump(student, file)

        return len(students)


def read_groups_information() -> list[str]:
    groups = []
    with open("groups.pickle", "rb") as file:
        while True:
            try:
                groups.append(pickle.load(file))
            except EOFError:
                break
    spec_names = set()
    for group in groups:
        spec_names.add(group.specialty.name)

    return list(spec_names)


def read_students_information() -> list[Student]:
    students = []
    with open("students.pickle", "rb") as file:
        while True:
            try:
                students.append(pickle.load(file))
            except EOFError:
                break

    return students
