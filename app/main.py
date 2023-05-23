from datetime import datetime
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
    birth_date: datetime
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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if groups:
        return [len(i.students) for i in groups][0]
    return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as f:
        data = pickle.load(f)

    return set([i.specialty.name for i in data])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        data = pickle.load(f)

    return data
