import io
from employee_parser import read_employee_data

def test_read_employee_data_with_mixed_headers(tmp_path):
    file_content = """id,email,name,department,hours_worked,salary
1,alice@example.com,Alice Johnson,Marketing,160,50
2,bob@example.com,Bob Smith,Design,150,40
"""

    file_path = tmp_path / "test.csv"
    file_path.write_text(file_content)

    result = read_employee_data(str(file_path))

    assert len(result) == 2
    assert result[0]["name"] == "Alice Johnson"
    assert result[0]["rate"] == 50
    assert result[1]["department"] == "Design"
