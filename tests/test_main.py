import sys
import json
from main import main


def test_main_payout_report(monkeypatch, tmp_path):
    # Создаем временный CSV-файл
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("name,department,hours,rate\nAlice,Marketing,160,50")

    # Создаем папку output
    output_dir = tmp_path / "output"
    output_dir.mkdir()

    # Путь к файлу без расширения (как ты хочешь — "report" -> "output/report.json")
    output_file = output_dir / "report"

    # Подменяем sys.argv
    monkeypatch.setattr(sys, "argv", [
        "main.py",
        str(csv_file),
        "--report", "payout",
        "--output", str(output_file.name)  # просто "report", не полный путь
    ])

    # Временно меняем рабочую директорию, чтобы main писал в tmp_path/output
    monkeypatch.chdir(tmp_path)

    # Запускаем main
    main()

    written_file = output_dir / "report.json"
    assert written_file.exists()

    with open(written_file) as f:
        data = json.load(f)

    assert any(dept["department"] == "Marketing" for dept in data)
    alice = next(emp for dept in data for emp in dept["employees"] if emp["name"] == "Alice")
    assert alice["payout"] == 8000
