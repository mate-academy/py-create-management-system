from dataclasses import dataclass
import pickle


@dataclass(frozen=True)
class Specialty:
    name: str
    number: int


@dataclass(frozen=True)
class Student:
    first_name: str
    last_name: str
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass(frozen=True)
class Group:
    specialty: Specialty
    course: str
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as dest:
        pickle.dump(groups, dest)
        if groups:
            return max(len(group.students) for group in groups)
        return 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as dest:
        pickle.dump(students, dest)
        return len(students)


def read_groups_information() -> set:
    with open("groups.pickle", "rb") as source:
        spec_lst = [group.specialty for group in pickle.load(source)]
        return set(spec.name for spec in spec_lst)


def read_students_information() -> list:
    with open("students.pickle", "rb") as source:
        return list(pickle.load(source))
