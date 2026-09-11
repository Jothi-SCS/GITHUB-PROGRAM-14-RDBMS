import os

def test_solution_exists():
    assert os.path.exists("solution.sql"), \
        "solution.sql file is missing"

def test_declare():
    with open("solution.sql", "r") as f:
        content = f.read().upper()

    assert "DECLARE" in content, \
        "DECLARE block missing"

def test_begin():
    with open("solution.sql", "r") as f:
        content = f.read().upper()

    assert "BEGIN" in content, \
        "BEGIN block missing"

def test_dbms_output():
    with open("solution.sql", "r") as f:
        content = f.read().upper()

    assert "DBMS_OUTPUT.PUT_LINE" in content, \
        "Output statement missing"

def test_addition():
    with open("solution.sql", "r") as f:
        content = f.read()

    assert "+" in content, \
        "Addition operation missing"
