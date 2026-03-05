from __future__ import annotations
from datetime import date, datetime
import itertools
from typing import List

class BorrowManager:

    def __init__(self):
        self.records: List = []
        self._id_counter = itertools.count(1)

    def generate_id(self) -> str: # simple sequential ID, no need to scan existing records
        return f"B{next(self._id_counter):03d}"

    # CRUD helpers
    def add(self, record) -> None:
        self.records.append(record)

    def find(self, bid: str):
        return next((r for r in self.records if r.id == bid), None)

    def mark_returned(self, bid: str) -> bool:
        rec = self.find(bid)
        if rec:
            rec.mark_returned()
            return True
        return False

    def delete(self, bid: str) -> bool:
        rec = self.find(bid)
        if rec:
            self.records.remove(rec)
            return True
        return False

    def all(self):
        return list(self.records)  # return copy if needed

    def sorted_by_return(self):
        return sorted(
            self.records,
            key=lambda r: datetime.strptime(r.return_date, "%Y-%m-%d"),
        )

    def stats(self):
        if not self.records:
            return [], [], []

        today = date.today()
        total = sum(r.quantity for r in self.records if not r.returned)

        upcoming = []
        overdue = []
        for r in self.records:
            if r.is_overdue:
                overdue.append(r)
            else:
                try:
                    rd = datetime.strptime(r.return_date, "%Y-%m-%d").date()
                    days = (rd - today).days
                    if 0 <= days <= 3 and not r.returned:
                        upcoming.append(r)
                except ValueError:
                    pass

        return [f"目前總借出數量：{total} 件"], upcoming, overdue