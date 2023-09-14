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
    course: int | str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        max_len = 0
        for group in groups:
            if len(group.students) > max_len:
                max_len = len(group.students)
            pickle.dump(group, file)
    return max_len


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as file:
        groups = []
        while True:
            try:
                group = pickle.load(file)
                groups.append(group)
            except EOFError:
                break

    specialts = []
    for group in groups:
        if group.specialty.name not in specialts:
            specialts.append(group.specialty.name)

    return specialts


def read_students_information() -> list:
    with open("students.pickle", "rb") as file:
        my_file = pickle.load(file)

    return my_file
