import pickle
from datetime import datetime
import dataclasses


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


def write_groups_information(list_of_groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(list_of_groups, f)
    return max((len(g.students) for g in list_of_groups), default=0)


def write_students_information(list_of_students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(list_of_students, f)
    return len(list_of_students)


def read_groups_information() -> list[str]:
    with open("groups.pickle", "rb") as f:
        names = set()
        while True:
            try:
                group = pickle.load(f)
            except EOFError:
                break

            if isinstance(group, list):
                for grp in group:
                    names.add(grp.specialty.name)
            else:
                names.add(group.specialty.name)
        return sorted(list(names))


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as f:
        students = []
        while True:
            try:
                obj = pickle.load(f)
            except EOFError:
                break
            if isinstance(obj, list):
                students.extend(obj)
            else:
                students.append(obj)
        return students
