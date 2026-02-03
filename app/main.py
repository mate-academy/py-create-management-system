from dataclasses import dataclass, field
from datetime import datetime
import pickle


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: int
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list = field(default_factory=list)

    def __post_init__(self) -> None:
        if not isinstance(self.course, int):
            raise TypeError(f"course must be int,"
                            f" not {type(self.course).__name__}")

        if not isinstance(self.students, list):
            raise TypeError(f"students must be list,"
                            f" not {type(self.students).__name__}")


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)
        if not groups:
            return 0
        return max(len(g.students) for g in groups)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)
        return len(students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)
        groups_specialty = []
        for grp in groups:
            grp = grp.specialty.name
            if not grp:
                continue
            groups_specialty.append(grp)
        groups_specialty = list(set(groups_specialty))
        return groups_specialty


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)
        return students
