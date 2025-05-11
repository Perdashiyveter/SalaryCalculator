from reports.payout import PayoutReport


def test_payout_report_generation():
    employees = [
        {"name": "Alice", "department": "Marketing", "hours": 160, "rate": 50},
        {"name": "Bob", "department": "Marketing", "hours": 150, "rate": 40},
        {"name": "Carol", "department": "Design", "hours": 170, "rate": 60},
    ]

    report = PayoutReport()
    report.generate(employees)
    result = report.result

    assert "Marketing" in result
    assert "Design" in result

    marketing_payout = sum(entry["payout"] for entry in result["Marketing"])
    design_payout = sum(entry["payout"] for entry in result["Design"])

    assert marketing_payout == (160*50 + 150*40)
    assert design_payout == 170*60
