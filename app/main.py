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
    birth_date: int
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
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            pickle.dump(group, pickle_file)

    return max([len(group.students) for group in groups], default=0)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> list[Group]:
    groups = []

    with open("groups.pickle", "rb") as pickle_file:

        while True:
            try:
                groups.append(pickle.load(pickle_file))
            except EOFError:
                break

    return list(set(group.specialty.name for group in groups))


def read_students_information() -> list[Student]:
    students = []

    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break

    return students
