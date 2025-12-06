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
    with open("groups.pickle", "wb") as file_to_write:
        pickle.dump(groups, file_to_write)

    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file_to_write:
        pickle.dump(students, file_to_write)

    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as file_to_read:
        groups = pickle.load(file_to_read)

    return set(group.specialty.name for group in groups)


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file_to_read:
        students = pickle.load(file_to_read)
    return students
