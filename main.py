import argparse
import json
from reports import get_report
from employee_parser import read_employee_data


def main():
    parser = argparse.ArgumentParser(description="Генератор зарплатного отчёта")
    parser.add_argument("files", nargs="+", help="CSV файлы с данными работников")
    parser.add_argument("--report", required=True, help='Тип отчёта (например "payout" - выплата)')
    parser.add_argument("--output", default="report", help='Имя выходного файла JSON для сохранения отчёта (по умолчанию - "report"')

    args = parser.parse_args()

    employees = []
    for file in args.files:
        data = read_employee_data(file)
        employees.extend(data)

    report = get_report(args.report)
    report.generate(employees)

    with open(f"output/{args.output}.json", "w") as f:
        json.dump(report.to_json(), f, ensure_ascii=False, indent=2)
        print(report)
        print("Отчёт сохранен в report.json")


if __name__ == "__main__":
    main()