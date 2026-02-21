from datetime import date, datetime
from collections import defaultdict

class BorrowManager:
    def __init__(self):
        self.records = []
        self.next_id_num = 1

    def _generate_id(self):
        while True:
            bid = f"B{self.next_id_num:03d}"
            if not any(r.get_id() == bid for r in self.records):
                self.next_id_num += 1
                return bid
            self.next_id_num += 1

    def add_record(self, record):
        self.records.append(record)

    def find_record(self, bid):
        for r in self.records:
            if r.get_id() == bid:
                return r
        return None

    def mark_returned(self, bid):
        record = self.find_record(bid)
        if record:
            record.mark_returned()
            return True
        return False

    def delete_record(self, bid):
        record = self.find_record(bid)
        if record:
            self.records.remove(record)
            return True
        return False

    def get_all_records(self):
        return self.records

    def get_records_by_return_date(self):
        return sorted(
            self.records,
            key=lambda r: datetime.strptime(r.get_return_date(), "%Y-%m-%d")
        )

    def get_stats(self):
        if not self.records:
            return [], [], []

        total_borrowed = 0
        upcoming = []
        overdue = []

        today = date.today()

        for r in self.records:
            if not r.is_returned():
                total_borrowed += r.get_quantity()

            try:
                ret_date = datetime.strptime(r.get_return_date(), "%Y-%m-%d").date()
                days_left = (ret_date - today).days
                if days_left < 0 and not r.is_returned():
                    overdue.append(r)
                elif 0 <= days_left <= 3 and not r.is_returned():
                    upcoming.append(r)
            except:
                pass

        borrow_lines = [f"目前總借出數量：{total_borrowed} 件"]

        return borrow_lines, upcoming, overdue