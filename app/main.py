import dataclasses
import pickle
from datetime import datetime
from typing import List, Any


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
    course: str
    students: List[Student] = None


def write_groups_information(groups: List[Group]) -> int | None:
    if not groups:
        return None

    max_students = max(len(group.students) for group in groups)

    group_info = []
    for group in groups:
        group_info.append({
            "specialty": group.specialty,
            "course": group.course,
            "students": group.students
        })

    try:
        with open("groups.pickle", "wb") as file:
            pickle.dump(group_info, file)

        return max_students
    except Exception as e:
        return None


def write_students_information(students: List[Student]) -> int | None:
    if not students:
        return None

    try:
        with open("students.pickle", "wb") as file:
            pickle.dump(students, file)

        return len(students)
    except Exception as e:
        return 0


def read_groups_information() -> List[Any]:
    with open("groups.pickle", "rb") as file:
        group_info = pickle.load(file)
    return group_info


def read_students_information() -> List[Any] | Any:
    try:
        with open("students.pickle", "rb") as file:
            students = pickle.load(file)

        return students
    except Exception as e:
        print(f"Error reading from pickle file: {e}")
        return []
