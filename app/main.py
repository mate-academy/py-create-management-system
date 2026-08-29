from dataclasses import dataclass
from datetime import datetime
import pickle


# =======================================
#               DATA CLASSES
# =======================================

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
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list  # list[Student]


# =======================================
#             REQUIRED FUNCTIONS
# =======================================

def write_groups_information(groups: list) -> int:
    """
    Writes the list of Group instances to 'groups.pickle'.
    Returns the maximum number of students in any group.
    """
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)

    if not groups:
        return 0

    return max(len(group.students) for group in groups)


def write_students_information(students: list) -> int:
    """
    Writes all Student instances into 'students.pickle'.
    Returns the number of students.
    """
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)

    return len(students)


def read_groups_information() -> list:
    """
    Reads groups from 'groups.pickle' and returns a list
    of specialties' names (without repetitions).
    """
    with open("groups.pickle", "rb") as f:
        groups: list[Group] = pickle.load(f)

    specialties = {group.specialty.name for group in groups}
    return list(specialties)


def read_students_information() -> list:
    """
    Reads students from 'students.pickle' and returns a list
    of Student class instances.
    """
    with open("students.pickle", "rb") as f:
        students: list[Student] = pickle.load(f)

    return students


# =======================================
#         OPTIONAL DEMO USAGE
# Remove this block before submission if needed.
# =======================================

if __name__ == "__main__":
    sp = Specialty("Computer Science", 101)

    st1 = Student("John", "Doe", datetime(2006,
                                          5,
                                          12), 9.2, True, "123456", "Kyiv")
    st2 = Student("Anna", "Ivanova", datetime(2005,
                                              8,
                                              3), 8.7, False, "987654", "Lviv")

    group = Group(sp, 1, [st1, st2])

    print(write_groups_information([group]))
    print(write_students_information([st1, st2]))
    print(read_groups_information())
    print(read_students_information())
