import json
from models.task import BorrowRecord

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        try:
            with open(self.file_name, 'r') as f:
                data = json.load(f)
            records = []
            for item in data:
                record = BorrowRecord(
                    item['id'],
                    item['borrower_name'],
                    item['student_id'],
                    item['admin_name'],
                    item['equipment_name'],
                    item['quantity'],
                    item['return_date']
                )
                if item.get('returned', False):
                    record.mark_returned()
                records.append(record)
            return records
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"讀取借用記錄失敗: {e}")
            return []

    def save(self, records):
        data = []
        for r in records:
            item = {
                'id': r.get_id(),
                'borrower_name': r.get_borrower_name(),
                'student_id': r.get_student_id(),
                'admin_name': r.get_admin_name(),
                'equipment_name': r.get_equipment_name(),
                'quantity': r.get_quantity(),
                'return_date': r.get_return_date(),
                'returned': r.is_returned()
            }
            data.append(item)
        try:
            with open(self.file_name, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print(f"儲存借用記錄失敗: {e}")