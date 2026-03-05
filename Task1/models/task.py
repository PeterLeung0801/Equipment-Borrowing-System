from __future__ import annotations
from datetime import datetime, date

class BorrowRecord:

    def __init__(self, id: str, borrower_name: str, student_id: str, admin_name: str,
                 equipment_name: str, quantity: int, return_date: str,
                 borrow_date: str = None, returned: bool = False):
        self.id = id
        self.borrower_name = borrower_name
        self.student_id = student_id
        self.admin_name = admin_name
        self.equipment_name = equipment_name.strip()
        self.quantity = int(quantity)
        self.return_date = return_date
        self.borrow_date = borrow_date or date.today().strftime("%Y-%m-%d")
        self.returned = returned

    def mark_returned(self) -> None:
        self.returned = True

    def is_overdue(self) -> bool:
        try:
            ret_date = datetime.strptime(self.return_date, "%Y-%m-%d").date()
            return ret_date < date.today() and not self.returned
        except ValueError:
            return False

    def __str__(self) -> str:
        status = " [已歸還]" if self.returned else ""
        overdue = " [逾期]" if self.is_overdue() else ""
        return (
            f"{self.equipment_name} (ID: {self.id}) | "
            f"借用人: {self.borrower_name} ({self.student_id}) | "
            f"管理員: {self.admin_name} | 數量: {self.quantity} | "
            f"借出: {self.borrow_date} | 歸還期限: {self.return_date}{overdue}{status}"
        )