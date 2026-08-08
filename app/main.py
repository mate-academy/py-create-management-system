from dataclasses import dataclass
from typing import List, Any
import pickle


@dataclass(unsafe_hash=True)
class Specialty:
    name: str
    number: int

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Specialty):
            return (self.name, self.number) < (other.name, other.number)
        return NotImplemented


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Group):
            return (self.specialty, self.course) < (
                other.specialty,
                other.course,
            )
        return NotImplemented


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    max_num = max(len(group.students) for group in groups) if groups else 0
    return max_num


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialties = list({group.specialty.name for group in groups})
    return specialties


def read_students_information() -> List[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students
