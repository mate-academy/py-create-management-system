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
    birth_date: str  # You can use a string for date
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list  # List of Student instances


def write_groups_information(groups: str) -> None:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    # Check if there are any groups
    if not groups:
        return 0  # Return 0 when there are no groups

    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: int) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> str:
    with open("groups.pickle", "rb") as f:
        groups = pickle.load(f)
    unique_specialties = set(group.specialty.name for group in groups)
    return list(unique_specialties)


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        students = pickle.load(f)
    return students
