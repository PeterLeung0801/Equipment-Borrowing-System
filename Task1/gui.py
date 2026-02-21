import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime, timedelta, date
from models.task import BorrowRecord
from models.priority_task import PriorityBorrowRecord  # 雖然移除 priority，但保留類別結構
from core.task_manager import BorrowManager
from core.file_handler import FileHandler

FILE_NAME = "borrows.json"
file_handler = FileHandler(FILE_NAME)
manager = BorrowManager()

loaded_records = file_handler.load()
for record in loaded_records:
    manager.add_record(record)

if loaded_records:
    max_num = max(int(r.get_id()[1:]) for r in loaded_records if r.get_id().startswith("B"))
    manager.next_id_num = max_num + 1

def refresh_list():
    listbox.delete(0, tk.END)
    records = manager.get_records_by_return_date()
    for r in records:
        listbox.insert(tk.END, r.display())
    update_stats()

def update_stats():
    borrow_lines, upcoming, overdue = manager.get_stats()
    stats_text.delete(1.0, tk.END)
    if borrow_lines:
        stats_text.insert(tk.END, "目前借出狀況：\n" + "\n".join("  " + line for line in borrow_lines) + "\n\n")
    if overdue:
        stats_text.insert(tk.END, "逾期未還：\n" + "\n".join("  " + r.display() for r in overdue) + "\n\n")
    if upcoming:
        stats_text.insert(tk.END, "即將到期（3天內）：\n" + "\n".join("  " + r.display() for r in upcoming))
    if not (borrow_lines or overdue or upcoming):
        stats_text.insert(tk.END, "目前無借用記錄")

def add_borrow():
    borrower_name = borrower_name_entry.get().strip()
    student_id = student_id_entry.get().strip()
    admin_name = admin_name_entry.get().strip()
    equipment_name = equipment_name_entry.get().strip()
    quantity = quantity_entry.get().strip()
    return_date_str = return_date_entry.get().strip()

    if not all([borrower_name, student_id, admin_name, equipment_name, quantity, return_date_str]):
        messagebox.showwarning("必填欄位", "所有欄位皆為必填")
        return

    try:
        qty = int(quantity)
        if qty <= 0:
            raise ValueError
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
        today = date.today()
        max_return = today + timedelta(days=30)
        if return_date > max_return:
            messagebox.showwarning("借用限制", "歸還日期最多只能設定為今天起 30 天內")
            return
        if return_date < today:
            messagebox.showwarning("日期錯誤", "歸還日期不能早於今天")
            return
    except ValueError:
        messagebox.showwarning("格式錯誤", "借用數量需為正整數\n歸還日期格式：YYYY-MM-DD")
        return

    bid = manager._generate_id()

    # 因為移除 priority，使用一般 BorrowRecord
    record = BorrowRecord(
        bid=bid,
        borrower_name=borrower_name,
        department=student_id,  # 暫用 department 欄位存學生編號
        quantity=qty,
        return_date=return_date_str,
        equipment_name=equipment_name
    )

    # 額外記錄管理員姓名（可擴展模型，但這裡先用 display 顯示）
    # 若要正式儲存，可在模型中新增 __admin_name 屬性

    manager.add_record(record)
    refresh_list()
    clear_entries()
    messagebox.showinfo("借用成功", f"借用記錄已新增\n編號：{bid}\n管理員：{admin_name}")

def clear_entries():
    borrower_name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    admin_name_entry.delete(0, tk.END)
    equipment_name_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    return_date_entry.delete(0, tk.END)

def mark_returned():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("操作", "請選擇一筆借用記錄")
        return
    text = listbox.get(sel[0])
    bid = text.split("(ID: ")[1].split(")")[0]
    if manager.mark_returned(bid):
        refresh_list()
        messagebox.showinfo("已歸還", f"記錄 {bid} 已標記為歸還")
    else:
        messagebox.showerror("錯誤", "找不到該記錄")

def delete_record():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("操作", "請選擇一筆借用記錄")
        return
    text = listbox.get(sel[0])
    bid = text.split("(ID: ")[1].split(")")[0]
    if manager.delete_record(bid):
        refresh_list()
        messagebox.showinfo("已刪除", f"記錄 {bid} 已刪除")
    else:
        messagebox.showerror("錯誤", "找不到該記錄")

def on_close():
    file_handler.save(manager.get_all_records())
    root.destroy()

# ───────────── GUI 介面 ─────────────
root = tk.Tk()
root.title("設備借用管理系統")
root.geometry("1150x750")
root.configure(bg="#f8f9fa")
root.protocol("WM_DELETE_WINDOW", on_close)

# 輸入區
input_frame = tk.Frame(root, bg="#f8f9fa")
input_frame.pack(pady=20, padx=30, fill=tk.X)

row = 0
labels = [
    "借用人姓名",
    "借用人學生編號",
    "設備管理員姓名",
    "設備名稱",
    "借用數量",
    "歸還日期 (YYYY-MM-DD，最多30天)"
]
entries = []

for label_text in labels:
    tk.Label(input_frame, text=label_text, bg="#f8f9fa", font=("Microsoft JhengHei", 11, "bold")) \
        .grid(row=row, column=0, sticky="w", pady=8, padx=(0, 12))
    entry = tk.Entry(input_frame, width=50, font=("Microsoft JhengHei", 11))
    entry.grid(row=row, column=1, pady=8, sticky="w")
    entries.append(entry)
    row += 1

borrower_name_entry, student_id_entry, admin_name_entry, equipment_name_entry, quantity_entry, return_date_entry = entries

# 按鈕區（並排）
btn_frame = tk.Frame(root, bg="#f8f9fa")
btn_frame.pack(pady=15)

buttons = [
    ("新增借用", add_borrow, "#28a745"),
    ("標記已歸還", mark_returned, "#007bff"),
    ("刪除記錄", delete_record, "#dc3545"),
    ("重新整理", refresh_list, "#6c757d")
]

for text, cmd, color in buttons:
    tk.Button(btn_frame, text=text, command=cmd, bg=color, fg="white",
              font=("Microsoft JhengHei", 12, "bold"), width=14, height=2) \
        .pack(side=tk.LEFT, padx=12)

# 統計區
stats_frame = tk.LabelFrame(root, text=" 借用狀態與警示 ", bg="#e9f7ff", padx=15, pady=12,
                            font=("Microsoft JhengHei", 12, "bold"))
stats_frame.pack(padx=30, pady=10, fill=tk.X)
stats_text = tk.Text(stats_frame, height=10, width=110, font=("Consolas", 10), bg="white", relief="flat")
stats_text.pack()

# 借用列表
listbox = tk.Listbox(root, font=("Consolas", 11), height=22, width=130, selectbackground="#d1e7ff")
listbox.pack(padx=30, pady=(10,20), fill=tk.BOTH, expand=True)

refresh_list()
root.mainloop()