from models.task import BorrowRecord

class PriorityBorrowRecord(BorrowRecord):
    # Legacy subclass for priority records.
    def __init__(self, id, borrower_name, student_id, admin_name, equipment_name, quantity, return_date):
        super().__init__(id, borrower_name, student_id, admin_name, equipment_name, quantity, return_date)

    def display(self):
        # Same as parent class (no priority display)
        return super().__str__()