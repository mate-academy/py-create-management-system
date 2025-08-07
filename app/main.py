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


def write_groups_information(info: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(info, file)

    return max((len(group.students) for group in info), default=0)


def write_students_information(info: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(info, f)

    return len(info)


def read_groups_information() -> set:
    specialties = set()
    with open("groups.pickle", "rb") as file:
        info = pickle.load(file)
        for group in info:
            specialties.add(group.specialty.name)
        return specialties


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        list_of_student = pickle.load(f)
    return list_of_student
