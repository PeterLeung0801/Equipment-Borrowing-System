# Task 1 – Equipment Borrowing Management System

## Description

This system is designed to help laboratories, departments, or university facilities manage the borrowing of equipment (such as oscilloscopes, 3D printers, projectors, tools, etc.).

It allows administrators to record borrowing details, track return dates, mark items as returned, and receive alerts for overdue or soon-due items.

## Core Functionalities

- Add new borrowing record (auto-generated ID: B001, B002, ...)
- Mark record as returned
- Delete borrowing record
- Display all records sorted by return date
- Show statistics and alerts (total borrowed quantity, overdue items, items due within 3 days)
- Persistent storage using JSON (auto-load on startup, save on exit)

## Input Fields

- Borrower Name (required)
- Student ID (required)
- Equipment Administrator Name (required)
- Equipment Name (required)
- Borrow Quantity (positive integer, required)
- Return Date (YYYY-MM-DD format, maximum 30 days from today, required)

## System Constraints

- Return date must be after today and no later than 30 days from the borrow date
- All fields are mandatory
- Overdue items are automatically flagged in display and statistics

## OOP Design Demonstrated

- **Encapsulation**: Private attributes with getter methods in `BorrowRecord`
- **Modular Programming**: Separation into `models/`, `core/`, `main.py`, and `gui.py`
- **Composition**: `BorrowManager` manages a collection of `BorrowRecord` objects
- **Data Persistence**: JSON-based save/load mechanism

## How to Run

- GUI version: `python Task1/gui.py`
- Console version: `python Task1/main.py`

Data is stored in `borrows.json` in the Task1 folder.