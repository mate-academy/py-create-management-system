import dataclasses
import datetime
import pickle


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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(list_group: list[Group]) -> int:
    with open("groups.pickle", "wb") as groups:
        pickle.dump(list_group, groups)
    if len(list_group) == 0:
        return 0
    return max([len(group.students) for group in list_group])


def write_students_information(list_students: list[Student]) -> int:
    with open("students.pickle", "wb") as students:
        pickle.dump(list_students, students)
    return len(list_students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as groups:
        list_of_group = pickle.load(groups)
    return set([group.specialty.name for group in list_of_group])


def read_students_information() -> list:
    with open("students.pickle", "rb") as students:
        list_of_student = pickle.load(students)
    return list_of_student
