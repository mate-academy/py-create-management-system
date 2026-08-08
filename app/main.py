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
    count_students = []
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups:
            count_students.append(len(group.students))
            pickle.dump(group, pickle_file)

    if not count_students:
        return 0
    return max(count_students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in students:
            pickle.dump(student, pickle_file)

    return len(students)


def read_groups_information() -> set:
    specialtys = []
    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                specialtys.append(pickle.load(pickle_file).specialty.name)
            except EOFError:
                break

    return set(specialtys)


def read_students_information() -> list:
    students = []
    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                students.append(pickle.load(pickle_file))
            except EOFError:
                break

    return students
