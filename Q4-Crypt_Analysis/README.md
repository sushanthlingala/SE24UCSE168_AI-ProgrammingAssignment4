# Q4 – Crypt-arithmetic Puzzle (CSP)

## Problem Statement

Implement the crypt-arithmetic puzzle (TWO + TWO = FOUR) using Constraint Satisfaction Problem (CSP) techniques as described in the textbook (Figure 6.2a).

---

## Approach

This problem models the crypt-arithmetic puzzle as a **Constraint Satisfaction Problem (CSP)** where each letter represents a unique digit.

* **Variables**: Distinct letters in the puzzle (F, T, U, W, R, O)
* **Domains**: Digits from 0 to 9
* **Constraints**:

  * Each letter must map to a unique digit (**Alldiff constraint**)
  * No leading digit can be zero (T ≠ 0, F ≠ 0)
  * The arithmetic equation must hold: TWO + TWO = FOUR

The solution is constructed using:

* **Backtracking Search** to assign digits to letters
* **Constraint Checking** to ensure validity during assignment
* **Early Pruning** to eliminate invalid partial assignments

The solver dynamically evaluates the numerical values of words and ensures the arithmetic constraint is satisfied.

---

## Files

| File           | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `csp_crypt.py` | Implementation of crypt-arithmetic puzzle solver using CSP |

---

## Setup

Run the program:

```bash id="q4setup"
python csp_crypt.py
```

---

## Running the Program

```id="q4menu"
*** Crypt-analysis Puzzle (Constraint Satisfaction Problem) ***

1. Find solution
2. Add new words
3. Show current words
4. Exit
```

**Recommended flow:** Option 1 → View solution

---

## CSP Representation

| Component       | Description                                      |
| --------------- | ------------------------------------------------ |
| Variables       | Letters in the puzzle (F, T, U, W, R, O)         |
| Domain          | Digits from 0 to 9                               |
| Constraints     | Alldiff + arithmetic equation + no leading zeros |
| Constraint Type | Global constraint (Alldiff)                      |

---

## Project Structure

```id="q4struct"
Q4-Crypt_Analysis/
├── csp_crypt.py
└── README.md
```

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
