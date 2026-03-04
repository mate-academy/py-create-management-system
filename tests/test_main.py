from app.main import write_students_information, read_students_information
from app.main import Student  # Specialty не нужен в этом тесте


def test_students_information_write_read() -> None:
    """Test writing and reading students information."""
    # Создаём тестовых студентов
    students = [
        Student(
            first_name="Alice",
            last_name="Smith",
            birth_date="2005-06-15",
            average_mark=4.5,
            has_scholarship=True,
            phone_number="1234567890",
            address="123 Main St",
        ),
        Student(
            first_name="Bob",
            last_name="Johnson",
            birth_date="2005-09-20",
            average_mark=4.0,
            has_scholarship=False,
            phone_number="0987654321",
            address="456 Park Ave",
        ),
    ]

    # Проверяем количество при записи
    count = write_students_information(students)
    assert count == 2

    # Проверяем чтение студентов
    loaded_students = read_students_information()
    assert len(loaded_students) == 2
    assert loaded_students[0].first_name == "Alice"
    assert loaded_students[1].first_name == "Bob"
