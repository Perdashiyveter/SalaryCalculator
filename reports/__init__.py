from .payout import PayoutReport

reports = {
    "payout": PayoutReport(),
}


def get_report(name: str):
    if name not in reports:
        raise ValueError(f"Неизвестный тип отчёта: {name}")
    return reports[name]