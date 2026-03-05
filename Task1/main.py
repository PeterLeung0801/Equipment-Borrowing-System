from datetime import datetime, timedelta, date

from core.file_handler import FileHandler
from core.task_manager import BorrowManager
from models.task import BorrowRecord

FILE_NAME = "borrows.json"


def prompt(text: str) -> str:
    # Wraps :func:`input` to strip whitespace.
    # Keeps the main loop clean by avoiding repeated ``.strip()`` calls.
    return input(text).strip()


def list_menu() -> None:
    # Display the main menu options in the terminal.
    print("\n=== 設備借用管理系統 (Console) ===")
    print("1. 新增")
    print("2. 標記歸還")
    print("3. 刪除")
    print("4. 顯示紀錄")
    print("5. 統計")
    print("6. 存檔並離開")


def validate_return_date(date_str: str) -> bool:
    # Check that the return date string is in YYYY‑MM‑DD format and within 30 days of today.
    try:
        rd = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today()
        return today <= rd <= today + timedelta(days=30)
    except ValueError:
        return False


def add_entry(manager: BorrowManager) -> None:
    # Collect data from the user and add a new record.
    data = {
        "borrower_name": prompt("借用人: "),
        "student_id": prompt("學生號: "),
        "admin_name": prompt("管理員: "),
        "equipment_name": prompt("設備: "),
        "quantity": prompt("數量: "),
        "return_date": prompt("歸還日(YYYY-MM-DD): "),
    }

    if not all(data.values()):
        print("欄位不可空白")
        return

    if not data["quantity"].isdigit() or int(data["quantity"]) <= 0:
        print("數量要正整數")
        return

    if not validate_return_date(data["return_date"]):
        print("日期格式或範圍錯誤")
        return

    bid = manager.generate_id()
    rec = BorrowRecord(bid, **data)
    manager.add(rec)
    print("新增好了", bid)


def main():
    fh = FileHandler(FILE_NAME)
    mgr = BorrowManager()

    for r in fh.load():
        mgr.add(r)

    # if file had ids, bump counter
    if mgr.records:
        last = max(int(r.id[1:]) for r in mgr.records if r.id.startswith("B"))
        mgr._id_counter = iter(range(last + 1, 9999))

    while True:
        list_menu()
        choice = prompt("選項: ")
        if choice == "1":
            add_entry(mgr)
        elif choice == "2":
            bid = prompt("哪個編號? ")
            print("歸還" if mgr.mark_returned(bid) else "沒找到")
        elif choice == "3":
            bid = prompt("要刪除? ")
            print("刪掉了" if mgr.delete(bid) else "沒找到")
        elif choice == "4":
            for r in mgr.sorted_by_return():
                print(r)
        elif choice == "5":
            lines, up, od = mgr.stats()
            print(*lines, sep="\n")
            if od:
                print("逾期:")
                print(*od, sep="\n")
            if up:
                print("即將到期:")
                print(*up, sep="\n")
        elif choice == "6":
            fh.save(mgr.all())
            break
        else:
            print("再輸入一次")


if __name__ == "__main__":
    main()