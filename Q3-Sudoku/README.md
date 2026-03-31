# Q3 – Sudoku Solver (CSP)

## Problem Statement

Implement the Sudoku puzzle using Constraint Satisfaction Problem (CSP) techniques as described in the textbook (Section 6.2.6).

---

## Approach

This problem models Sudoku as a **Constraint Satisfaction Problem (CSP)** with 81 variables representing the cells of a 9×9 grid.

* **Variables**: A1 to I9 (each cell in the grid)
* **Domains**: Values from 1 to 9
* **Constraints**:

  * All values in each row must be different
  * All values in each column must be different
  * All values in each 3×3 subgrid must be different

These constraints are represented using **27 Alldiff constraints** (9 rows, 9 columns, 9 subgrids).

The algorithm uses:

* **AC-3 (Arc Consistency)** to reduce domains initially
* **Backtracking Search** to assign values
* **Forward Checking** to eliminate invalid assignments early
* **MRV (Minimum Remaining Values)** heuristic for efficient variable selection

The solver first applies constraint propagation and then completes the solution using backtracking if required.

---

## Files

| File            | Description                                          |
| --------------- | ---------------------------------------------------- |
| `csp_sudoku.py` | Implementation of Sudoku solver using CSP techniques |

---

## Setup

Run the program:

```bash id="q3setup"
python csp_sudoku.py
```

---

## Running the Program

```id="q3menu"
*** Sudoku CSP ***

1. Load textbook puzzle
2. Enter custom puzzle
3. Solve
4. Show current puzzle
5. Exit
```

**Recommended flow:** Option 1 → Option 3

---

## CSP Representation

| Component       | Description                                  |
| --------------- | -------------------------------------------- |
| Variables       | 81 cells (A1 to I9)                          |
| Domain          | Values from 1 to 9                           |
| Constraints     | Row, Column, and 3×3 box Alldiff constraints |
| Constraint Type | Global constraint (Alldiff)                  |

---

## Project Structure

```id="q3struct"
Q3-Sudoku/
├── csp_sudoku.py
└── README.md
```

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
