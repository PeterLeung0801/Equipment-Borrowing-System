# Equipment Borrowing Management System

**Author**: Leung Kam Chung Peter  
**Course**: COMP8090SEF – Data Structures and Algorithms  
**Pre-submission Version**

---

## Project Overview

This repository contains two independent tasks:

- **Task 1** – Equipment Borrowing Management System (OOP-based application)
- **Task 2** – Self-study on Heap Data Structure and Heap Sort Algorithm

This project is newly developed for COMP8090SEF and is not based on any previous coursework submission.

---

## Task 1 – OOP-based Application Development

### Problem Definition

University laboratories and departments often face challenges in tracking who borrows equipment, when it is due back, and whether items are overdue. Without a proper system, equipment may be lost, returned late, or over-borrowed.

This system provides a structured way to record, monitor, and manage equipment borrowing with clear alerts and statistics.

### Key Features

- Add new borrowing record (auto ID generation)
- Mark as returned
- Delete record
- List all records sorted by return date
- Statistics & alerts (total borrowed quantity, overdue, soon due)
- Persistent JSON storage

### OOP Concepts Demonstrated

- **Encapsulation**: Private attributes (`__bid`, `__borrower_name`, `__student_id`, etc.) with public getter methods to control access and ensure data integrity.
- **Modular Programming**: Clear separation of concerns using packages/folders (`models/`, `core/`) and separate files for data models, business logic, file handling, and user interfaces.
- **Composition**: The `BorrowManager` class composes and manages a collection of `BorrowRecord` objects, demonstrating "has-a" relationships.
- **Single Responsibility Principle**: Each class has a focused responsibility (e.g., `BorrowRecord` handles individual record data, `FileHandler` handles persistence, `BorrowManager` handles business operations).
- **Data Abstraction**: Users interact with high-level methods (e.g., `add_record`, `mark_returned`) without needing to know internal implementation details.

### How to Run Task 1

- GUI Version  
  `python Task1/gui.py`

- Console Version  
  `python Task1/main.py`

Data is stored in `borrows.json` in the Task1 folder.

---

## Task 2 – Self Study

### Selected Data Structure
Max Heap

### Selected Algorithm
Heap Sort

The Heap data structure and Heap Sort algorithm are implemented and analyzed, including time complexity and practical applications.

### How to Run Task 2

`python Task2/heap_sort.py`

---

**Note**:  
Task 1 demonstrates practical application of **Object-Oriented Programming** principles in a real-world management system, while Task 2 focuses on core data structures and algorithms knowledge required in the course.