import dataclasses
from datetime import datetime
import pickle


# чтоб сделать обьект хэшируемым и использовать set
@dataclasses.dataclass(frozen=True)
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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(group_info: list) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(group_info, file)

    if not group_info:
        return 0

    num_of_students = max(len(group.students) for group in group_info)

    return num_of_students


def write_students_information(student_info: list) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(student_info, file)

    return len(student_info)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        info = pickle.load(file)

    list_of_specialties = {group.specialty.name for group in info}
    return list(list_of_specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        info = pickle.load(file)

    return list(info)
