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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_students_information(students_list: list) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(students_list, f)
    return len(students_list)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        users = pickle.load(f)
        return users


def write_groups_information(group_list: list) -> None:
    max_st = 0
    with open("groups.pickle", "wb") as f:
        pickle.dump(group_list, f)
    for group in group_list:
        if len(group.students) > max_st:
            max_st = len(group.students)
    return max_st


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        group = pickle.load(f)
    specialties = set()
    for i in group:
        specialties.add(i.specialty.name)
    return specialties
