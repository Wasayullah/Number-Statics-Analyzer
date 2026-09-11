# Number Statistics Analyzer

A beginner Python project that takes a list of numbers from the user and analyzes them — pure Python, no libraries.

## Features

- Total numbers
- Sum
- Average
- Maximum / Minimum
- Even / Odd numbers
- Positive / Negative numbers / Zeros
- Count of each category

## File Structure

```
Number-Statistics-Analyzer/
│
├── Number_Statistics_Analyzer.ipynb
│
└── README.md
```

## How to Run

1. Open `Number_Statistics_Analyzer.ipynb` in Jupyter Notebook or JupyterLab.
2. Run all cells (`Kernel` -> `Restart & Run All`).
3. Enter numbers separated by commas, e.g.: `10, 25, -5, 8, 0, 12, -3, 10`
4. Read the analysis report.

## Example Output

```
========== NUMBER ANALYSIS ==========

Numbers: [10, 25, -5, 8, 0, 12, -3, 10]

Total Numbers : 8
Sum           : 57
Average       : 7.125

Maximum       : 25
Minimum       : -5

Even Numbers  : [10, 8, 0, 12, 10]
Odd Numbers   : [25, -5, -3]

Positive      : [10, 25, 8, 12, 10]
Negative      : [-5, -3]
Zeros         : [0]

Number of each category:
  Even count     : 5
  Odd count      : 3
  Positive count : 5
  Negative count : 2
  Zero count     : 1

=====================================
```

## What You Learn

```
input()
   ↓
strings
   ↓
lists
   ↓
loops
   ↓
if / elif / else
   ↓
functions
   ↓
statistics
```

Built entirely with functions instead of one large code cell — a good first step toward data analysis.