import pytest
from utils.db_connection import get_db_connection


@pytest.fixture
def db():
    connection = get_db_connection()
    try:
        yield connection
    finally:
        connection.close()


def test_database_connection(db):
    assert db.is_connected()


def test_employee_exists(db):
    cursor = db.cursor()
    try:
        cursor.execute(
            "SELECT employee_name FROM automation_employees "
            "WHERE employee_id = %s",
            (101,)
        )
        result = cursor.fetchone()
        assert result is not None
        assert result[0] == "John Smith"
    finally:
        cursor.close()


def test_employee_salary(db):
    cursor = db.cursor()
    try:
        cursor.execute(
            "SELECT salary FROM automation_employees "
            "WHERE employee_id = %s",
            (102,)
        )
        result = cursor.fetchone()
        assert result is not None
        assert float(result[0]) == 95000.00
    finally:
        cursor.close()


def test_mandatory_fields(db):
    cursor = db.cursor()
    try:
        cursor.execute("""
            SELECT COUNT(*)
            FROM automation_employees
            WHERE employee_name IS NULL
               OR department IS NULL
               OR salary IS NULL
        """)
        assert cursor.fetchone()[0] == 0
    finally:
        cursor.close()


def test_employee_count(db):
    cursor = db.cursor()
    try:
        cursor.execute(
            "SELECT COUNT(*) FROM automation_employees"
        )
        assert cursor.fetchone()[0] == 3
    finally:
        cursor.close()
