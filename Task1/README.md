# Task 1 – Equipment Borrowing System

A simple app to manage borrowing equipment.

Features:
- Add records
- Mark returned
- Delete
- List sorted by date
- Stats
- JSON save/load

OOP: classes for records, manager, file handler.

Run: `python main.py` or `python gui.py`
  are public, and there are methods for marking a record returned and
  checking overdue status.  The `__str__` method produces the textual
  representation used by the interfaces.

- `core/task_manager.py` : a lightweight in-memory repository.  It
  generates sequential IDs, tracks a list of records, and provides
  helper methods for querying, sorting, deleting, and gathering
  statistics (total quantity, upcoming due, overdue).

- `core/file_handler.py` : handles loading and saving the record list
  to `borrows.json` using the `json` module.  Conversion between
  dictionaries and dataclass instances is automatic using
  `dataclasses.asdict` and keyword unpacking (`BorrowRecord(**item)`).

- `main.py` : a simple command‑line program that displays a numbered
  menu, reads user input, validates it, and calls the manager/file
  handler accordingly.  Helper functions keep the loop short and
  readable.

- `gui.py` : builds a Tkinter window with entry fields, buttons, and a
  listbox.  Event handlers call the same manager/file handler APIs
  used by the console version, so logic is shared.

- `borrows.json` : runtime data file.  You can inspect it manually; it
  contains a JSON array of objects corresponding to `BorrowRecord`
  fields.


## Requirements

Python 3.10 or above
Standard Python libraries:
  json
  datetime
  dataclasses
  tkinter (for GUI)

The console version only requires Python standard libraries.
The GUI version requires Tkinter support.

## How to Run

- GUI version: `python Task1/gui.py`
- Console version: `python Task1/main.py`

Data is stored in `borrows.json` in the Task1 folder.