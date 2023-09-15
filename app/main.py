from typing import List

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
    course: str
    students: List[Student]


groups_data = [
    Group(
        Specialty("Financess_and_credit", 11),
        "1/1",
        [
            Student("Petr", "Antonov", datetime(2000, 1, 10), 10.2,
                    True, "122-33-44", "Kiev Bloka 11/10"),
            Student("Anna", "Nicolaeva", datetime(2000, 2, 21), 10.5,
                    True, "221-31-41", "Kiev Bloka 4/18"),
            Student("Lena", "Isaeva", datetime(2001, 3, 14), 7.2,
                    False, "433-54-46", "Odessa Parkova 3/45"),
            Student("Ury", "Ursky", datetime(2001, 6, 25), 7.1,
                    False, "511-82-27", "Odessa Parkova 16/20"),
        ]
    ),
    Group(
        Specialty("Financess_and_credit", 11),
        "1/1",
        [
            Student("Oleg", "Antonov", datetime(2001, 3, 25), 10.7,
                    True, "112-33-26", "Rovno Bloka 35/6"),
            Student("Inna", "Dmitrenko", datetime(2000, 7, 21), 9.4,
                    True, "121-82-55", "Rovno Bloka 17/4"),
            Student("July", "Egorova", datetime(2001, 10, 14), 8.2,
                    True, "489-58-66", "Ternopol Sadova 65/5"),
            Student("Pavel", "Andreev", datetime(2001, 6, 25), 7.1,
                    False, "561-12-11", "Ternopol Sadova 27/2"),
            Student("Dmitry", "Petrov", datetime(2000, 2, 17), 7.0,
                    False, "589-34-38", "Ternopol Bloka 8/23"),
        ]
    ),
    Group(
        Specialty("Banks_works", 11),
        "2/1",
        [
            Student("Ura", "Orlov", datetime(2001, 2, 7), 9.5,
                    True, "289-233-564", "Dnipro Gradska 23/35"),
            Student("Ksenia", "Ivanova", datetime(2001, 7, 4), 8.7,
                    True, "727-31-44", "Kiev Sadova 27/9"),
            Student("Vika", "Saenko", datetime(2001, 5, 23), 8.9,
                    True, "633-55-66", "Kiev Parkova 14/55"),
            Student("Ivan", "Dmitrov", datetime(2000, 4, 14), 7.2,
                    False, "916-42-38", "Dnipro Markova 18/3"),
            Student("Tania", "Fedorova", datetime(2001, 7, 3), 8.4,
                    False, "231-93-67", "Dnipro Markova 4/15"),
        ]
    )
]

students_data = [
    Student("Petr", "Antonov", datetime(2000, 1, 10), 10.2,
            True, "122-33-44", "city Kiev Bloka 11/10"),
    Student("Anna", "Nicolaeva", datetime(2000, 2, 21), 10.5,
            True, "221-31-41", "city Kiev Bloka 4/18"),
    Student("Lena", "Isaeva", datetime(2001, 3, 14), 7.2,
            False, "433-54-46", "city Odessa Parkova 3/45"),
    Student("Ury", "Ursky", datetime(2001, 6, 25), 7.1,
            False, "511-82-27", "city Odessa Parkova 16/20"),
    Student("Oleg", "Antonov", datetime(2001, 3, 25), 10.7,
            True, "112-33-26", "city Rovno Bloka 35/6"),
    Student("Inna", "Dmitrenko", datetime(2000, 7, 21), 9.4,
            True, "121-82-55", "city Rovno Bloka 17/4"),
    Student("July", "Egorova", datetime(2001, 10, 14), 8.2,
            True, "489-58-66", "city Ternopol Sadova 65/5"),
    Student("Pavel", "Andreev", datetime(2001, 6, 25), 7.1,
            False, "561-12-11", "city Ternopol Sadova 27/2"),
    Student("Dmitry", "Petrov", datetime(2000, 2, 17), 7.0,
            False, "589-34-38", "city Ternopol Bloka 8/23"),
    Student("Ura", "Orlov", datetime(2001, 2, 7), 9.5,
            True, "289-233-564", "city Dnipro Gradska 23/35"),
    Student("Ksenia", "Ivanova", datetime(2001, 7, 4), 8.7,
            True, "727-31-44", "city Kiev Sadova 27/9"),
    Student("Vika", "Saenko", datetime(2001, 5, 23), 8.9,
            True, "633-55-66", "city Kiev Parkova 14/55"),
    Student("Ivan", "Dmitrov", datetime(2000, 4, 14), 7.2,
            False, "916-42-38", "city Dnipro Markova 18/3"),
    Student("Tania", "Fedorova", datetime(2001, 7, 3), 8.4,
            False, "231-93-67", "city Dnipro Markova 4/15"),
]


def write_groups_information(data: List[Group]) -> int:

    with open("groups.pickle", "wb") as write:
        pickle.dump(data, write)

    if data:
        return max([len(elem.students) for elem in data if data])
    return 0


write_groups_information(groups_data)


def write_students_information(data: Student) -> int:
    with open("students.pickle", "wb") as write:
        pickle.dump(data, write)
    count_students = len(data)
    return count_students


write_students_information(students_data)


def read_groups_information() -> str:
    specialytys = []
    with open("groups.pickle", "rb") as read:
        students_spec_info = pickle.load(read)

    specialytys = set([elem.specialty.name for elem in students_spec_info])
    return specialytys


read_groups_information()


def read_students_information() -> Student:

    with open("students.pickle", "rb") as read:
        list_students = pickle.load(read)

    return list_students


read_students_information()
