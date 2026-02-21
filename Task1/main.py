from models.task import BorrowRecord
from core.task_manager import BorrowManager
from core.file_handler import FileHandler
from datetime import datetime, timedelta, date

def main():
    FILE_NAME = "borrows.json"
    file_handler = FileHandler(FILE_NAME)
    manager = BorrowManager()

    loaded_records = file_handler.load()
    for record in loaded_records:
        manager.add_record(record)

    if loaded_records:
        max_num = max(int(r.get_id()[1:]) for r in loaded_records if r.get_id().startswith("B"))
        manager.next_id_num = max_num + 1

    while True:
        print("\n=== 設備借用管理系統 (Console) ===")
        print("1. 新增借用記錄")
        print("2. 標記已歸還")
        print("3. 刪除記錄")
        print("4. 顯示所有借用記錄（按歸還日期排序）")
        print("5. 顯示統計與警示")
        print("6. 儲存並退出")

        choice = input("\n請輸入選項 (1-6): ").strip()

        if choice == "1":
            borrower_name = input("借用人姓名: ").strip()
            student_id = input("借用人學生編號: ").strip()
            admin_name = input("設備管理員姓名: ").strip()
            equipment_name = input("設備名稱: ").strip()
            quantity_str = input("借用數量: ").strip()
            return_date_str = input("歸還日期 (YYYY-MM-DD，最多30天): ").strip()

            if not all([borrower_name, student_id, admin_name, equipment_name, quantity_str, return_date_str]):
                print("所有欄位皆為必填！")
                continue

            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    raise ValueError
                return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
                today = date.today()
                max_date = today + timedelta(days=30)
                if return_date > max_date:
                    print("歸還日期最多只能是今天起 30 天內！")
                    continue
                if return_date < today:
                    print("歸還日期不能早於今天！")
                    continue
            except ValueError:
                print("數量必須是正整數，日期格式必須是 YYYY-MM-DD")
                continue

            bid = manager._generate_id()
            record = BorrowRecord(bid, borrower_name, student_id, admin_name, equipment_name, quantity, return_date_str)
            manager.add_record(record)
            print(f"借用記錄新增成功！編號：{bid}")

        elif choice == "2":
            bid = input("輸入要標記歸還的借用編號 (如 B001): ").strip()
            if manager.mark_returned(bid):
                print(f"記錄 {bid} 已標記為已歸還")
            else:
                print("找不到該記錄")

        elif choice == "3":
            bid = input("輸入要刪除的借用編號 (如 B001): ").strip()
            if manager.delete_record(bid):
                print(f"記錄 {bid} 已刪除")
            else:
                print("找不到該記錄")

        elif choice == "4":
            records = manager.get_records_by_return_date()
            if not records:
                print("目前無借用記錄")
                continue
            print("\n=== 所有借用記錄（按歸還日期排序） ===")
            for r in records:
                print(r.display())

        elif choice == "5":
            borrow_lines, upcoming, overdue = manager.get_stats()
            print("\n=== 統計與警示 ===")
            if borrow_lines:
                for line in borrow_lines:
                    print(line)
            if overdue:
                print("\n逾期未還：")
                for r in overdue:
                    print("  " + r.display())
            if upcoming:
                print("\n即將到期（3天內）：")
                for r in upcoming:
                    print("  " + r.display())
            if not (borrow_lines or overdue or upcoming):
                print("目前無借用記錄或警示")

        elif choice == "6":
            file_handler.save(manager.get_all_records())
            print("已儲存所有記錄，再見！")
            break

        else:
            print("無效選項，請重新輸入")

if __name__ == "__main__":
    main()