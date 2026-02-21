from datetime import datetime, date

class BorrowRecord:
    def __init__(self, bid, borrower_name, student_id, admin_name, equipment_name, quantity, return_date):
        self.__bid = bid
        self.__borrower_name = borrower_name
        self.__student_id = student_id
        self.__admin_name = admin_name
        self.__equipment_name = equipment_name.strip()
        self.__quantity = int(quantity)
        self.__return_date = return_date
        self.__borrow_date = date.today().strftime("%Y-%m-%d")
        self.__returned = False

    def get_id(self):
        return self.__bid

    def get_borrower_name(self):
        return self.__borrower_name

    def get_student_id(self):
        return self.__student_id

    def get_admin_name(self):
        return self.__admin_name

    def get_equipment_name(self):
        return self.__equipment_name

    def get_quantity(self):
        return self.__quantity

    def get_return_date(self):
        return self.__return_date

    def get_borrow_date(self):
        return self.__borrow_date

    def is_returned(self):
        return self.__returned

    def mark_returned(self):
        self.__returned = True

    def display(self):
        status = " [已歸還]" if self.__returned else ""
        overdue = ""
        try:
            ret_date = datetime.strptime(self.__return_date, "%Y-%m-%d").date()
            if ret_date < date.today() and not self.__returned:
                overdue = " [逾期]"
        except:
            pass

        return (f"{self.__equipment_name} (ID: {self.__bid}) | "
                f"借用人: {self.__borrower_name} ({self.__student_id}) | "
                f"管理員: {self.__admin_name} | 數量: {self.__quantity} | "
                f"借出: {self.__borrow_date} | 歸還期限: {self.__return_date}{overdue}{status}")