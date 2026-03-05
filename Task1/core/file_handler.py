import json
from models.task import BorrowRecord

class FileHandler:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def load(self) -> list[BorrowRecord]:
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                raw = json.load(f)
            records = []
            for item in raw:
                record = BorrowRecord(**item)
                records.append(record)
            return records
        except FileNotFoundError:
            return []
        except Exception as e:
            print("Failed to load borrow records:", e)
            return []

    def save(self, records: list[BorrowRecord]) -> None:
        try:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                data = []
                for r in records:
                    item = {
                        'id': r.id,
                        'borrower_name': r.borrower_name,
                        'student_id': r.student_id,
                        'admin_name': r.admin_name,
                        'equipment_name': r.equipment_name,
                        'quantity': r.quantity,
                        'return_date': r.return_date,
                        'borrow_date': r.borrow_date,
                        'returned': r.returned
                    }
                    data.append(item)
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Failed to save borrow records:", e)