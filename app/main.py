# write your code here
import dataclasses
from datetime import date
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: date
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
    try:
        with open("groups.pickle", "wb") as file:
            pickle.dump(groups, file)

        return max(len(group.students) for group in groups)

    except Exception as e:
        print(f"Error occurred while writing groups information: {e}")
        return 0


def write_students_information(students: List[Student]) -> int:
    try:
        with open("students.pickle", "wb") as file:
            pickle.dump(students, file)

        return len(students)

    except Exception as e:
        print(f"Error occurred while writing student information: {e}")
        return 0


def read_groups_information() -> List[str]:
    try:
        with open("groups.pickle", "rb") as file:
            groups: List[Group] = pickle.load(file)

        return list(set(group.specialty.name for group in groups))

    except Exception as e:
        print(f"Error occurred while readig groups infomation: {e}")
        return []


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as file:
            students: List[Student] = pickle.load(file)

        return students

    except Exception as e:
        print(f"Error occurred while reading students information: {e}")
        return []
