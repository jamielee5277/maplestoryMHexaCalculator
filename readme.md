# Stat Level-Up Probability Calculator

This Python script calculates probabilities for leveling up stats in a game where each level-up randomly increases one of three stats: one **main stat** and two **normal stats**. The script uses dynamic programming to compute exact probabilities based on the current stat levels and the game’s leveling rules.

---

## Features

- Computes **exact probabilities** (not a simulation).
- Three outputs in percentages:
  1. Probability that **main stat hits level 10**.
  2. Probability that **at least one normal stat hits level 10**.
  3. Probability that **main stat reaches level 8 or higher** (8, 9, or 10).
- Supports **optional starting stat levels**.
- Automatically calculates remaining level-ups (20 total level-ups in all cases).
- Command-line interface (CLI) for easy usage.

---

## Level-Up Rules

- Every level-up increases **exactly one stat**.
- Main stat leveling chances depend on its current level:

| Main Stat Level | Chance to Level Main Stat |
|-----------------|--------------------------|
| 0–2             | 35%                      |
| 3–6             | 20%                      |
| 7               | 15%                      |
| 8               | 10%                      |
| 9               | 5%                       |
| 10              | 0%                       |

- Remaining probability is split equally among normal stats (up to level 10).
- Total level-ups: **20**.
- The script ensures that starting stats do not exceed total level-ups.

---

## Requirements

- Python 3.7+  
- No external dependencies (uses only standard library modules: `argparse` and `functools`).

---

## 🚀 Usage

### Prerequisites
* Python 3.6+

### Execution
Pass your current stats as arguments. The script calculates results based on a total of 20 level-up events.

```bash
# Example: Starting with Main Level 4, Normal1 Level 4, and Normal2 Level 3
```
python3 stats.py --main 4 --n1 4 --n2 3
```
