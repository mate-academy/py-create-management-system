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
    course: str
    students: list[Student]


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(list_of_groups, file)
    return max((
        len(group.students) for group in list_of_groups), default=0)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(list_of_students, file)
    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        specialtes = list(set(group.specialty.name for group in groups))
    return sorted(specialtes)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
    return students
