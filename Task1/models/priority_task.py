from models.task import BorrowRecord

class PriorityBorrowRecord(BorrowRecord):
    """保留檔案結構，實際已移除 priority，與 BorrowRecord 完全相同"""
    def __init__(self, bid, borrower_name, student_id, admin_name, equipment_name, quantity, return_date):
        super().__init__(bid, borrower_name, student_id, admin_name, equipment_name, quantity, return_date)

    def display(self):
        # 與父類別相同（無 priority 顯示）
        return super().display()