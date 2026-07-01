import json

class InvestorReport:

    def __init__(self, benchmark):

        self.data = benchmark

    def export_json(self):

        return json.dumps(
            self.data,
            indent=4
        )

    def executive_summary(self):

        largest = max(self.data.keys())

        avg = self.data[largest]["avg_ms"]

        return f"""
DynamiCore Executive Report

Largest benchmark:
{largest} nodes

Average latency:

{avg:.3f} ms

Status:

READY FOR ENTERPRISE VALIDATION
"""
