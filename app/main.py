import dataclasses
from datetime import datetime
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
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    """Writes group information to 'groups.pickle'
    and returns max student count."""
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    if not groups:
        return 0  # Повертаємо 0, якщо список порожній
    max_students = max(len(group.students) for group in groups)
    return max_students


def write_students_information(students: list[Student]) -> int:
    """Writes student information to 'students.pickle'
    and returns student count."""
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> set[str]:
    """Reads group information from 'groups.pickle'
    and returns unique specialty names."""
    try:
        with open("groups.pickle", "rb") as f:
            groups: list[Group] = pickle.load(f)
        specialty_names = {group.specialty.name for group in groups}
        return specialty_names
    except FileNotFoundError:
        return set()


def read_students_information() -> list[Student]:
    """Reads student information from 'students.pickle'
    and returns a list of Student instances."""
    try:
        with open("students.pickle", "rb") as f:
            students: list[Student] = pickle.load(f)
        return students
    except FileNotFoundError:
        return []
