import dataclasses
import pickle
from datetime import datetime
from typing import List


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
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    """
    Writes all inputted information about the Lyceum groups
    to the file named "groups.pickle".
    Returns the maximum number of students from all the groups.
    """
    with open("groups.pickle", "wb") as file:
        pickle.dump(groups, file)

    return max((len(group.students) for group in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    """
    Writes information about students to the "students.pickle" file.
    Returns the number of students.
    """
    with open("students.pickle", "wb") as file:
        pickle.dump(students, file)

    return len(students)


def read_groups_information() -> List[str]:
    """
    Reads data from the "groups.pickle" file.
    Returns all groups' specialties' names without repetition.
    """
    with open("groups.pickle", "rb") as file:
        groups = pickle.load(file)

    specialty_names = {group.specialty.name for group in groups}
    return list(specialty_names)


def read_students_information() -> List[Student]:
    """
    Reads data from the "students.pickle" file.
    Returns a list of all the Student class instances.
    """
    with open("students.pickle", "rb") as file:
        students = pickle.load(file)

    return students


if __name__ == "__main__":
    spec1 = Specialty(name="Computer Science", number=101)
    spec2 = Specialty(name="Mathematics", number=102)

    s1 = Student(
        first_name="Alice",
        last_name="Smith",
        birth_date=datetime(2004, 5, 17),
        average_mark=4.5,
        has_scholarship=True,
        phone_number="123-456",
        address="123 Main St",
    )

    s2 = Student(
        first_name="Bob",
        last_name="Brown",
        birth_date=datetime(2003, 8, 9),
        average_mark=3.9,
        has_scholarship=False,
        phone_number="987-654",
        address="456 Elm St",
    )

    s3 = Student(
        first_name="Charlie",
        last_name="Johnson",
        birth_date=datetime(2004, 11, 23),
        average_mark=4.2,
        has_scholarship=True,
        phone_number="555-555",
        address="789 Oak St",
    )

    g1 = Group(specialty=spec1, course=1, students=[s1, s2])
    g2 = Group(specialty=spec2, course=2, students=[s3])

    print("Max students in a group:", write_groups_information([g1, g2]))
    print("Number of students saved:", write_students_information([s1, s2, s3]))
    print("Specialties in groups:", read_groups_information())
    print("Loaded students:", read_students_information())
