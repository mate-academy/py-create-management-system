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
    specialty: "Specialty"
    course: int
    students: list[Student]


def write_groups_information(groups: list) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0
    return max(len(group.students) for group in groups)


def write_students_information(students: list) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        empty_set = set()
        for group in pickle.load(f):
            empty_set.add(group.specialty.name)
    return empty_set


def read_students_information() -> None:
    with open("students.pickle", "rb") as f:
        return pickle.load(f)
