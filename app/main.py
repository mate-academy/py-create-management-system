import dataclasses
from datetime import datetime
import pickle
from typing import List, Set, Dict, Any


@dataclasses.dataclass
class Specialty:
    name: str
    number: str


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
    max_students = 0
    try:
        with open("groups.pickle", "wb") as f:
            pickle.dump(groups, f)
        for group in groups:
            if len(group.students) > max_students:
                max_students = len(group.students)
        print(f"Groups information successfully written to groups.pickle. "
              f"Max students in a group: {max_students}")
        return max_students
    except IOError as e:
        print(f"Error writing groups information to file: {e}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred while writing groups: {e}")
        return 0


def write_students_information(students: List[Student]) -> int:
    try:
        with open("students.pickle", "wb") as f:
            pickle.dump(students, f)
        print(f"Students information successfully written to students.pickle. "
              f"Total students: {len(students)}")
        return len(students)
    except IOError as e:
        print(f"Error writing students information to file: {e}")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred while writing students: {e}")
        return 0


def read_groups_information() -> Set[str]:
    specialty_names: Set[str] = set()
    try:
        with open("groups.pickle", "rb") as f:
            groups: List[Group] = pickle.load(f)
        for group in groups:
            specialty_names.add(group.specialty.name)
        print(f"Groups information successfully read from groups.pickle. "
              f"Unique specialties: {specialty_names}")
        return specialty_names
    except FileNotFoundError:
        print("Error: 'groups.pickle' file not found.")
        return set()
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error reading or unpickling groups information: {e}")
        return set()
    except Exception as e:
        print(f"An unexpected error occurred while reading groups: {e}")
        return set()


def read_students_information() -> List[Student]:
    try:
        with open("students.pickle", "rb") as f:
            students: List[Student] = pickle.load(f)
        (print(f"Students information successfully "
               f"read from students.pickle. "
              f"Total students: {len(students)}"))
        return students
    except FileNotFoundError:
        print("Error: 'students.pickle' file not found.")
        return []
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error reading or unpickling students information: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading students: {e}")
        return []


if __name__ == "__main__":
    # --- Example Usage ---

    # 1. Create Specialty instances
    specialty_cs = \
        (Specialty(name="Computer Science", number="121"))
    specialty_math = \
        (Specialty(name="Applied Mathematics", number="113"))

    # 2. Create Student instances
    student1 = Student(
        first_name="Alice",
        last_name="Smith",
        birth_date=datetime(2003, 5, 15),
        average_mark=4.7,
        has_scholarship=True,
        phone_number="123-456-7890",
        address="123 Main St"
    )
    student2 = Student(
        first_name="Bob",
        last_name="Johnson",
        birth_date=datetime(2002, 11, 22),
        average_mark=3.9,
        has_scholarship=False,
        phone_number="098-765-4321",
        address="456 Oak Ave"
    )
    student3 = Student(
        first_name="Charlie",
        last_name="Brown",
        birth_date=datetime(2004, 1, 1),
        average_mark=4.2,
        has_scholarship=True,
        phone_number="555-123-4567",
        address="789 Pine Ln"
    )
    student4 = Student(
        first_name="Diana",
        last_name="Prince",
        birth_date=datetime(2003, 7, 30),
        average_mark=4.9,
        has_scholarship=True,
        phone_number="111-222-3333",
        address="Wonderland Rd"
    )

    group_cs_1 = Group(
        specialty=specialty_cs,
        course=3,
        students=[student1, student3]
    )
    group_math_2 = Group(
        specialty=specialty_math,
        course=2,
        students=[student2, student4]
    )
    group_cs_4 = Group(
        specialty=specialty_cs,
        course=4,
        students=[student4]
    )

    all_groups = [group_cs_1, group_math_2, group_cs_4]
    all_students = [student1, student2, student3, student4]

    print("\n--- Writing Information ---")
    max_students_in_group = \
        (write_groups_information(all_groups))
    num_students_written = \
        (write_students_information(all_students))

    print("\n--- Reading Information ---")
    read_specialties = read_groups_information()
    read_students = read_students_information()

    print("\n--- Verification ---")
    print(f"Max students reported by "
          f"write_groups_information: {max_students_in_group}")
    print(f"Number of students reported "
          f"by write_students_information: {num_students_written}")
    print(f"Unique specialties read: {read_specialties}")
    print(f"Number of students read: {len(read_students)}")
