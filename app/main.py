import dataclasses
import datetime
import typing
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime.datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int | str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int | datetime.datetime
    students: typing.List[Student]


def write_groups_information(groups: list[Group]) -> int:
    students_list = []
    for group in groups:
        for student in group.students:
            if student not in students_list:
                students_list.append(student)
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return len(students_list)


def write_students_information(students: list[Group]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list[Specialty]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
        print(type(groups))
    all_specialyty = []
    for group in groups:
        if group.specialty.name not in all_specialyty:
            all_specialyty.append(group.specialty.name)
    return all_specialyty


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
