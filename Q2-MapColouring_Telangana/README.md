# Q2 – Map Colouring (Telangana Districts)

## Problem Statement

Apply the Map Colouring problem using Constraint Satisfaction Problem (CSP) techniques to the 33 districts of Telangana.

---

## Approach

Map Colouring CSP is applied for the 33 districts of Telangana.

* **Variables**: 33 districts of Telangana
* **Domains**: A set of colours (may be user-defined, but are Red, Green, Blue, Black and White by default; minimum 3 required)
* **Constraints**: Adjacent districts must not share the same colour

The adjacency list for districts is stored in a JSON file to avoid cluttering within the code and keep it clean.

The algorithm uses:

* **AC-3 (Arc Consistency)** for initial constraint propagation
* **Backtracking Search** to assign colours
* **Forward Checking** to prune invalid values early
* **MRV (Minimum Remaining Values)** heuristic for efficient variable selection

---

## Files

| File                 | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| `csp_tg.py`          | Implementation of Map Colouring CSP for Telangana districts |
| `telangana_adj.json` | Adjacency list representing district neighbours             |

---

## Setup

Run the program:

```bash
python csp_tg.py
```
---

## Running the Program

```
*** Map Colouring Problem for the 33 Districts of Telangana ***

1. Solve with Current Colours
2. Set Custom Colours
3. Display All Districts
4. Display Colours in Current Colour Set
5. Exit
```

**Recommended flow:** Option 1 → View solution

---

## CSP Representation

| Component     | Description                                    |
| ------------- | ---------------------------------------------- |
| Variables     | 33 districts of Telangana                      |
| Domain        | Colours (user-defined, minimum 3 required)     |
| Constraints   | Adjacent districts must have different colours |
| Data Handling | Adjacency list stored externally in JSON            |

---

## Project Structure

```
Q2-MapColouring_Telangana/
├── csp_tg.py
├── telangana_adj.json
└── README.md
```

---

## Author

Sushanth Lingala
Roll No: **SE24UCSE168**
Course: **CS-2201 – Artificial Intelligence**
