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
    birth_date: datetime.datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int | datetime.datetime
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    max_number_of_students = None
    if groups:
        max_number_of_students = max([len(group.students) for group in groups])
    else:
        max_number_of_students = []
    with open("groups.pickle", "wb") as file_out:
        pickle.dump(groups, file_out)
    return max_number_of_students


def read_groups_information() -> set[Specialty]:
    groups = None
    with open("groups.pickle", "rb") as file_in:
        groups = pickle.load(file_in)

    unique_specialty_names = list(
        set(group.specialty.name for group in groups)
    )
    return unique_specialty_names or []


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_out:
        pickle.dump(students, file_out)
    return len(students)


def read_students_information() -> list[Student]:
    students = None
    with open("students.pickle", "rb") as file_in:
        students = pickle.load(file_in)
    return students
