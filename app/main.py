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
    phone_number: int
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(all_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(all_groups, f)
    if not all_groups:
        return 0
    return max(len(group.students) for group in all_groups)


def write_students_information(all_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(all_students, f)
    return len(all_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    all_specialities = []
    for group in groups:
        if group.specialty.name not in all_specialities:
            all_specialities.append(group.specialty.name)
    return all_specialities


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
