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

def write_groups_information(groups) -> int:
    with open('groups.pickle', 'wb') as f:
        pickle.dump(groups, f)
    max_students = max(len(group.students) for group in groups)
    return max_students

def write_students_information(students) -> int:
    with open('students.pickle', 'wb') as f:
        pickle.dump(students, f)
    return len(students)

def read_groups_information(groups) -> int:
    with open("groups.pickle", "rb") as f:
        pickle.load(groups, f)
    new_group = {group.specialty for group in groups}
    return list(new_group)
def read_students_information(students) -> list:
    with open("students.pickle", "wb") as f:
        students = pickle.load(f)
    return students
