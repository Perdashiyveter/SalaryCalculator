from .base import BaseReport


class PayoutReport(BaseReport):
    def generate(self, employees: list[dict]):
        report = {}
        for employee in employees:
            department = employee["department"]
            payout = employee["hours"] * employee["rate"]
            report.setdefault(department, []).append({
                "name": employee["name"],
                "hours": employee["hours"],
                "rate": employee["rate"],
                "payout": payout
            })
        self.result = report

    def __str__(self):
        lines = []
        for department, people in self.result.items():
            lines.append(department)
            total_hours = 0
            total_payout = 0
            for person in people:
                lines.append(
                    f"-------------- {person['name']:<20} {person['hours']:<6} {person['rate']:<6} ${person['payout']}"
                )
                total_hours += person["hours"]
                total_payout += person["payout"]
            lines.append(f"{'':>36}{total_hours:<13} ${total_payout}")
            lines.append("")
        return "\n".join(lines)

    def to_json(self):
        result = []
        for department, people in self.result.items():
            total_hours = sum(p["hours"] for p in people)
            total_payout = sum(p["payout"] for p in people)
            result.append({
                "department": department,
                "employees": people,
                "total_hours": total_hours,
                "total_payout": total_payout
            })
        return result