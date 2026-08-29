import dataclasses
from datetime import datetime
import pickle
from typing import List


# -------------------- DATA CLASSES --------------------

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
    students: List[Student]


# -------------------- FUNCTIONS --------------------

def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    # return maximum number of students in a group
    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    # unique specialty names
    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students
