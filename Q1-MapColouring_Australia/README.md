# Q1 – Map Colouring (Australia)

## Problem Statement

Implement the Map Colouring problem using Constraint Satisfaction Problem (CSP) techniques for the seven principal states and territories of Australia: WA, NT, Q, SA, NSW, V, T.

---

## Approach

This problem models the Map Colouring task as a **Constraint Satisfaction Problem (CSP)** where each state or territory is treated as a variable and assigned a colour from a finite domain.

* **Variables**: WA, NT, SA, Q, NSW, V, T
* **Domains**: A set of colours (default: Red, Green, Blue)
* **Constraints**: Adjacent regions must not share the same colour

The adjacency relationships between states are represented using a constraint graph. The solution ensures that no two neighbouring states have the same colour.

The algorithm combines:

* **AC-3 (Arc Consistency)** for domain reduction
* **Backtracking Search** for finding a valid assignment
* **Forward Checking** to eliminate invalid values early
* **MRV (Minimum Remaining Values)** heuristic for efficient variable selection

Tasmania (T) has no adjacent states, and hence has no constraints restricting its colour assignment.

---

## Files

| File         | Description                                                                  |
| ------------ | ---------------------------------------------------------------------------- |
| `csp_aus.py` | Implementation of Map Colouring CSP for Australia with AC-3 and backtracking |

---

## Setup

Run the program:

```bash
python csp_aus.py
```

---

## Running the Program

```
*** Map Colouring Problem for the 7 Principal States and Territories of Australia ***

1. Solve with Current Colours
2. Set Custom Colours
3. Display Colours in Current Colour Set
4. Exit
```

**Recommended flow:** Option 1 → View solution

---

## CSP Representation

| Component    | Description                                       |
| ------------ | ------------------------------------------------- |
| Variables    | WA, NT, SA, Q, NSW, V, T                          |
| Domain       | Colours (user-defined, minimum 3 required)        |
| Constraints  | Adjacent states must have different colours       |
| Special Case | Tasmania has no neighbours (independent variable) |

---

## Project Structure

```
Q1-MapColouring_Australia/
├── csp_aus.py
└── README.md
```

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**

---
