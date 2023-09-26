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
    birth_date: str
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: list


def write_groups_information(groups: str) -> None:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if groups:
        max_students = max(len(group.students) 
                           for group in groups)
        return max_students
    else:
        return 0  # Return 0 if there are no groups


def write_students_information(students: str) -> None:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> None:
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
        # Extract and return a list of unique specialty names
        specialty_names = list(set(group.specialty.name 
                                   for group in groups))
        return specialty_names
    except FileNotFoundError:
        return []


def read_students_information() -> None:
    try:
        with open("students.pickle", "rb") as f:
            students = pickle.load(f)
        return students
    except FileNotFoundError:
        return []
