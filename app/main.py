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


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as destination_file:
        pickle.dump(groups, destination_file)

    students_amount = 0

    for group in groups:
        if len(group.students) > students_amount:
            students_amount = len(group.students)

    return students_amount


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as destination_file:
        pickle.dump(students, destination_file)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as destination_file:
        loaded_group = pickle.load(destination_file)

    return set([group.specialty.name for group in loaded_group])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as destination_file:
        loaded_group = pickle.load(destination_file)

    return loaded_group
