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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    max_students = 0
    for group in list_of_groups:
        if len(group.students) > max_students:
            max_students = len(group.students)
    return max_students


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    groups_speciality = []
    for group in groups:
        groups_speciality.append(group.specialty.name)
    return set(groups_speciality)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
