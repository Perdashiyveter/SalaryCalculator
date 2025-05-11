def fix_header(header: str) -> str:
    header = header.strip().lower()
    if header in {'rate', 'hourly_rate', 'salary'}:
        return 'rate'
    elif header == 'hours_worked':
        return "hours"
    else:
        return header


def read_employee_data(filepath: str) -> list[dict]:
    with open(filepath, "r") as f:
        lines = f.readlines()

    if not lines:
        return []

    headers = [fix_header(header) for header in lines[0].strip().split(',')]
    data = []

    for line in lines[1:]:
        values = line.strip().split(",")
        row = dict(zip(headers, values))

        employee = {
            "name": row.get("name", "").strip(),
            "department": row.get("department", "").strip(),
            "hours": int(row.get("hours", 0)),
            "rate": int(row.get("rate", 0))
        }
        data.append(employee)

    return data
