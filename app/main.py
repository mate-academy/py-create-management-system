import dataclasses
from datetime import datetime
import pickle
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
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max((len(g.students) for g in groups), default=0)


def write_students_information(students: List[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    try:
        with open("groups.pickle", "rb") as f:
            return list({g.specialty.name for g in pickle.load(f)})
    except FileNotFoundError:
        return []


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    spec1: Specialty = Specialty("CS", 101)
    spec2: Specialty = Specialty("Math", 102)
    s1: Student = Student("Ivan", "Petrenko", datetime(2005, 5, 15), 4.5,
                          True, "+380661234567", "Kyiv")
    s2: Student = Student("Olena", "Shevchenko", datetime(2006, 3, 22), 4.0,
                          False, "+380671234567", "Lviv")
    s3: Student = Student("Mykola", "Ivanov", datetime(2005, 9, 10), 4.8,
                          True, "+380681234567", "Odesa")

    g1: Group = Group(spec1, 2, [s1, s2])
    g2: Group = Group(spec2, 1, [s3])
    groups: List[Group] = [g1, g2]
    students: List[Student] = [s1, s2, s3]

    print(f"Max students: {write_groups_information(groups)}")
    print(f"Total students: {write_students_information(students)}")
    print(f"Specialties: {read_groups_information()}")
    print(f"First student: {read_students_information()[0].first_name}")
