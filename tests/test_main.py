import pytest
import os
import unittest.mock

from datetime import date
from app.Specialty import Specialty

import app.main
from app.main import (
    Student,
    Group,
    write_groups_information,
    write_students_information,
    read_groups_information,
    read_students_information,
)


def basic_student(
    first_name="Ivan",
    last_name="Ivanov",
    birth_date=date.today(),
    mark=87.5,
    has_scholarship=False,
    phone="+380999999999",
    city="Kyiv",
):
    return Student(
        first_name, last_name, birth_date, mark, has_scholarship, phone, city
    )


@pytest.fixture
def specialty_init():
    return Specialty("Math and Physic", 1)


@pytest.fixture
def student_init():
    return basic_student()


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if os.path.exists(self.filename):
            os.remove(self.filename)


@pytest.mark.parametrize(
    "attribute",
    [
        "name",
        "number"
    ]
)
def test_specialty_instance(attribute, specialty_init):
    assert hasattr(
        specialty_init, attribute
    ), f"Specialty instance should have attribute '{attribute}'"


@pytest.mark.parametrize(
    "attribute,attr_type",
    [
        ("name", str),
        ("number", int)
    ]
)
def test_specialty_instance_type(attribute, attr_type, specialty_init):
    assert isinstance(
        getattr(specialty_init, attribute), attr_type
    ), f"Specialty instance attribute '{attribute}' should be {attr_type}"


@pytest.mark.parametrize(
    "attribute",
    [
        "first_name",
        "last_name",
        "birth_date",
        "average_mark",
        "has_scholarship",
        "phone_number",
        "address",
    ],
)
def test_student_instance(attribute, student_init):
    assert hasattr(
        student_init, attribute
    ), f"Student instance should have attribute '{attribute}'"


@pytest.mark.parametrize(
    "attribute,attr_type",
    [
        ("first_name", str),
        ("last_name", str),
        ("birth_date", date),
        ("average_mark", float),
        ("has_scholarship", bool),
        ("phone_number", str),
        ("address", str),
    ],
)
def test_student_instance_type(attribute, attr_type, student_init):
    assert isinstance(
        getattr(student_init, attribute), attr_type
    ), f"Specialty instance attribute '{attribute}' should be {attr_type}"


@pytest.mark.parametrize(
    "attribute",
    [
        "specialty",
        "course",
        "students",
    ],
)
def test_group_instance(attribute, specialty_init, student_init):
    group = Group(specialty_init, 1, [student_init])

    assert hasattr(
        group, attribute
    ), f"Group instance should have attribute '{attribute}'"


@pytest.mark.parametrize(
    "attribute,attr_type",
    [
        ("specialty", Specialty),
        ("course", int),
        ("students", list),
    ],
)
def test_group_instance_type(attribute, attr_type, specialty_init, student_init):
    group = Group(specialty_init, 1, [student_init])

    assert isinstance(
        getattr(group, attribute), attr_type
    ), f"Specialty instance attribute '{attribute}' should be {attr_type}"


@pytest.mark.parametrize(
    "kwargs,result",
    [
        ([Group(specialty=Specialty("Math and Physic", 1), course=1, students=[])], 0),
        (
            [
                Group(
                    specialty=Specialty("Math and Physic", 1),
                    course=1,
                    students=[basic_student()],
                )
            ],
            1,
        ),
        (
            [
                Group(
                    specialty=Specialty("English", 2),
                    course=2,
                    students=[
                        basic_student(),
                        basic_student(first_name="Mariia", mark=72.9),
                        basic_student(first_name="Dariia", mark=100.0),
                    ],
                ),
                Group(
                    specialty=Specialty("Biology", 2),
                    course=1,
                    students=[basic_student()],
                ),
            ],
            3,
        ),
    ],
)
def test_write_groups_information(kwargs, result):
    max_students_count = write_groups_information(kwargs)
    assert max_students_count == result, (
        f"Function write_groups_information must return a number of max students quantity in the group, "
        f"expected: {result}, but actual returned {max_students_count}"
    )


@pytest.mark.parametrize(
    "group",
    [
        Group(specialty=Specialty("Math and Physic", 1), course=1, students=[]),
        Group(
            specialty=Specialty("Biology", 2),
            course=1,
            students=[basic_student()],
        ),
    ],
)
def test_write_groups_information_created_file(group):
    with CleanUpFile("groups.pickle"):
        open_mock = unittest.mock.mock_open()

        with unittest.mock.patch("app.main.open", open_mock, create=True):
            app.main.write_groups_information([group])

        open_mock.assert_called_with("groups.pickle", "wb")


@pytest.mark.parametrize(
    "students,result",
    [
        ([], 0),
        (
            [basic_student()],
            1,
        ),
        (
            [
                basic_student(),
                basic_student(first_name="Mariia", mark=72.9),
                basic_student(first_name="Dariia", mark=100.0),
            ],
            3,
        ),
    ],
)
def test_write_students_information(students, result):
    students_count = write_students_information(students)
    assert students_count == result, (
        f"Function write_students_information must return a number of students, "
        f"expected: {result} but actual returned: {students_count}"
    )


@pytest.mark.parametrize(
    "students",
    [
        [],
        [basic_student()],
        [
            basic_student(),
            basic_student(first_name="Mariia", mark=72.9),
            basic_student(first_name="Dariia", mark=100.0),
        ],
    ],
)
def test_write_students_information_created_file(students):
    with CleanUpFile("students.pickle"):
        open_mock = unittest.mock.mock_open()

        with unittest.mock.patch("app.main.open", open_mock, create=True):
            app.main.write_students_information(students)

        open_mock.assert_called_with("students.pickle", "wb")


@pytest.mark.parametrize(
    "groups,result",
    [
        ([], []),
        (
            [Group(specialty=Specialty("Math and Physic", 1), course=1, students=[])],
            ["Math and Physic"],
        ),
        (
            [
                Group(
                    specialty=Specialty("Biology", 2),
                    course=1,
                    students=[basic_student()],
                ),
                Group(
                    specialty=Specialty("English", 1),
                    course=2,
                    students=[
                        basic_student(),
                        basic_student(first_name="Mariia", mark=72.9),
                        basic_student(first_name="Dariia", mark=100.0),
                    ],
                ),
            ],
            ["Biology", "English"],
        ),
        (
            [
                Group(
                    specialty=Specialty("English", 1),
                    course=2,
                    students=[
                        basic_student(),
                        basic_student(first_name="Mariia", mark=72.9),
                        basic_student(first_name="Dariia", mark=100.0),
                    ],
                ),
                Group(
                    specialty=Specialty("English", 2),
                    course=1,
                    students=[basic_student()],
                ),
            ],
            ["English"],
        ),
    ],
)
def test_read_groups_information(groups, result):
    with CleanUpFile("groups.pickle"):

        write_groups_information(groups)
        specialties = read_groups_information()
        assert sorted(specialties) == sorted(result), (
            f"Function read_groups_information must return a list of all specialties names, "
            f"expected: {result}, but actual returned: {specialties}"
        )


@pytest.mark.parametrize(
    "students",
    [
        [],
        [
            basic_student()
        ],
        [
            basic_student(),
            basic_student(first_name="Mariia", mark=72.9),
            basic_student(first_name="Dariia", mark=100.0),
        ],
    ],
)
def test_read_students_information(students):

    with CleanUpFile("students.pickle"):
        write_students_information(students)
        students_list = read_students_information()

        assert students_list == students, (
            f"Function read_students_information must return a list of all students, "
            f"expected: {students}, but actual returned: {students_list} "
        )
