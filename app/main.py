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


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups_of_students: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        for group in groups_of_students:
            pickle.dump(group, pickle_file)

    return max(
        ((len(group.students)) for group in groups_of_students), default=0
    )


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        for student in list_of_students:
            pickle.dump(student, pickle_file)

    return len(list_of_students)


def read_groups_information() -> list:
    groups_list = []
    specialties = []

    with open("groups.pickle", "rb") as pickle_file:
        while True:
            try:
                group = pickle.load(pickle_file)
                groups_list.append(group)
            except EOFError:
                break

    for group in groups_list:
        specialties.append(group.specialty.name)
    return list(set(specialties))


def read_students_information() -> list:
    students_list = []

    with open("students.pickle", "rb") as pickle_file:
        while True:
            try:
                student = pickle.load(pickle_file)
                students_list.append(student)
            except EOFError:
                break
    return students_list
