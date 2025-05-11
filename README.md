# Salary Report Calculator

Консольное Python-приложение для генерации зарплатных отчётов из CSV-файлов.

Также реализовано:
1. Создание отчёта в виде JSON файла
2. Возможность легко создавать новые виды отчётов

## Запуск

Если вы пользуетесь PyCharm, то нужно вводить параметры конфигурации в Edit Configurations.

```bash
python3 main.py data/data1.csv data/data2.csv data/data3.csv --report payout
```

Если вы хотите дать свое название для отчёта в виде JSON файла, то также нужно указать параметр --output, например

```bash
python3 main.py data/data1.csv data/data2.csv data/data3.csv --report payout --output report2
```

## Тестирование

```bash
pytest --cov=. --cov-report=term-missing
```

## Структура проекта

```
SalaryCalculator/
├── data/               # Входные CSV-файлы
├── output/             # Выходные отчёты
├── reports/            # Модули генерации отчётов
├── tests/              # Тесты
├── screenshots/        # Примеры работы программы с изображениями
├── employee_parser.py  # Файл, отвечающий за парсинг данных
├── main.py             # Главный файл запуска
└── README.md
```
