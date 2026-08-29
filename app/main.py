import dataclasses
import pickle
from datetime import datetime
from typing import List, Set


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


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    max_students = max(
        len(group.students) for group in groups
    ) if groups else 0
    return max_students


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> Set[str]:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)

    return {group.specialty.name for group in groups}


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)

    return students


# Example Usage
if __name__ == "__main__":
    # Create some specialties
    specialty1 = Specialty(name="Computer Science", number=101)
    specialty2 = Specialty(name="Mathematics", number=102)

    # Create some students
    student1 = Student(
        first_name="John",
        last_name="Doe",
        birth_date=datetime(2002, 5, 15),
        average_mark=85.5,
        has_scholarship=True,
        phone_number="123-456-7890",
        address="123 Elm St"
    )

    student2 = Student(
        first_name="Jane",
        last_name="Smith",
        birth_date=datetime(2003, 7, 22),
        average_mark=90.0,
        has_scholarship=False,
        phone_number="098-765-4321",
        address="456 Oak St"
    )
