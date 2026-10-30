# Introduction to Artificial Intelligence – Practicals

A collection of 10 beginner-friendly Python practicals for the subject **Introduction to Artificial Intelligence**, B.Sc. Business AI (Semester III), Institute of Science, Dr. Homi Bhabha State University, Mumbai.

| | |
|---|---|
| **Name** | Yash Baban Agre |
| **Class** | SY B.Sc. Business AI |
| **Seat No.** | 31470002 |
| **Semester** | III |
| **Guide** | Prof. Pooja Malha |

---

## Table of Contents

1. [About the Project](#about-the-project)
2. [Repository Structure](#repository-structure)
3. [Requirements](#requirements)
4. [Setup](#setup)
5. [How to Run](#how-to-run)
6. [Practicals Overview](#practicals-overview)
7. [Sample Outputs](#sample-outputs)
8. [Original Journal](#original-journal)

---

## About the Project

This repository contains the complete code of the AI practical journal. It starts with Python basics, then covers classic AI topics: search algorithms, game playing, knowledge representation, probability, machine learning, clustering and natural language processing. It ends with a small chatbot project.

Every program is a single `.py` file with simple comments that explain each step.

## Repository Structure

```
Introduction-to-Artificial-Intelligence-Practicals/
│
├── README.md                  <- You are here
├── requirements.txt           <- Python libraries needed
├── .gitignore                 <- Files Git should ignore
│
├── practicals/                <- All 10 Python programs
│   ├── practical_01_python_basics.py
│   ├── practical_02_bfs_dfs.py
│   ├── practical_03_a_star_search.py
│   ├── practical_04_tictactoe_minimax.py
│   ├── practical_05_knowledge_representation.py
│   ├── practical_06_naive_bayes.py
│   ├── practical_07_regression_decision_tree.py
│   ├── practical_08_kmeans_clustering.py
│   ├── practical_09_basic_nlp.py
│   └── practical_10_mini_ai_project.py
│
├── outputs/                   <- Saved output of each program
│   └── practical_01_output.txt ... practical_10_output.txt
│
└── docs/
    ├── YASH_AGRE_AI_MANUAL.pdf    <- Original journal (PDF)
    └── GITHUB_UPLOAD_GUIDE.md     <- How to upload this to GitHub
```

## Requirements

- **Python 3.9 or newer** (tested on Python 3.13)
- These libraries (listed in `requirements.txt`):
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `matplotlib`

Practicals 2 to 5 and 10 use only Python's built-in features. Practicals 1, 6, 7, 8 and 9 need the libraries above.

## Setup

1. Install Python from [python.org](https://www.python.org/downloads/). On Windows, tick **"Add Python to PATH"** during installation.
2. Check the installation by opening a terminal (Command Prompt on Windows) and typing:
   ```
   python --version
   ```
3. Open a terminal **inside the repository folder** and install the libraries:
   ```
   pip install -r requirements.txt
   ```

> On some Mac/Linux systems, use `python3` and `pip3` instead of `python` and `pip`.

## How to Run

From inside the repository folder, run any practical with:

```
python practicals/practical_01_python_basics.py
```

Change the file name to run a different practical. You can also open any file in **VS Code** or **Jupyter Notebook** and run it from there.

| Practical | Command |
|---|---|
| 1 | `python practicals/practical_01_python_basics.py` |
| 2 | `python practicals/practical_02_bfs_dfs.py` |
| 3 | `python practicals/practical_03_a_star_search.py` |
| 4 | `python practicals/practical_04_tictactoe_minimax.py` |
| 5 | `python practicals/practical_05_knowledge_representation.py` |
| 6 | `python practicals/practical_06_naive_bayes.py` |
| 7 | `python practicals/practical_07_regression_decision_tree.py` |
| 8 | `python practicals/practical_08_kmeans_clustering.py` |
| 9 | `python practicals/practical_09_basic_nlp.py` |
| 10 | `python practicals/practical_10_mini_ai_project.py` |

## Practicals Overview

| No. | Topic | File | Libraries |
|---|---|---|---|
| 1 | Python for AI – Setup and Basics | [`practical_01_python_basics.py`](practicals/practical_01_python_basics.py) | numpy, pandas, scikit-learn, matplotlib |
| 2 | Implementing BFS and DFS | [`practical_02_bfs_dfs.py`](practicals/practical_02_bfs_dfs.py) | built-in only |
| 3 | Implementing A* Search | [`practical_03_a_star_search.py`](practicals/practical_03_a_star_search.py) | built-in only |
| 4 | Solving Tic-Tac-Toe using Minimax | [`practical_04_tictactoe_minimax.py`](practicals/practical_04_tictactoe_minimax.py) | built-in only |
| 5 | Knowledge Representation using Prolog/Python | [`practical_05_knowledge_representation.py`](practicals/practical_05_knowledge_representation.py) | built-in only |
| 6 | Bayes Rule and Naive Bayes Classifier | [`practical_06_naive_bayes.py`](practicals/practical_06_naive_bayes.py) | pandas, scikit-learn |
| 7 | Linear Regression and Decision Tree | [`practical_07_regression_decision_tree.py`](practicals/practical_07_regression_decision_tree.py) | pandas, scikit-learn |
| 8 | K-Means Clustering | [`practical_08_kmeans_clustering.py`](practicals/practical_08_kmeans_clustering.py) | pandas, scikit-learn |
| 9 | Basic Natural Language Processing | [`practical_09_basic_nlp.py`](practicals/practical_09_basic_nlp.py) | pandas, scikit-learn |
| 10 | Mini AI Project (Chatbot) | [`practical_10_mini_ai_project.py`](practicals/practical_10_mini_ai_project.py) | built-in only |

### Practical 1: Python for AI – Setup and Basics
**Aim:** Set up the Python AI environment and practice the core data structures and libraries.
Verifies the installation, then practises lists, dictionaries, sets, NumPy arrays and Pandas Series/DataFrames using a small product-sales example.

### Practical 2: Implementing BFS and DFS
**Aim:** Represent a graph in Python and implement Breadth-First Search and Depth-First Search.
A city map is stored as an adjacency list. BFS (queue) and DFS (recursion) traverse it, and BFS also finds the shortest path from *Central* to *SouthEast*.

### Practical 3: Implementing A* Search
**Aim:** Find the optimal path on a grid using a heuristic.
A warehouse grid has obstacles. A* uses the Manhattan distance heuristic and a priority queue (`heapq`) ordered by `f(n) = g(n) + h(n)` to find the shortest path (cost 8).

### Practical 4: Solving Tic-Tac-Toe using Minimax
**Aim:** Build a Tic-Tac-Toe game whose AI never loses.
Implements Minimax with Alpha-Beta pruning. The AI (O) maximises and the human (X) minimises. A sample game is simulated move by move.

### Practical 5: Knowledge Representation using Prolog/Python
**Aim:** Represent facts and rules and perform logical inference.
An office hierarchy is stored as facts. The program defines `is_parent` and `is_ancestor` rules, and performs **forward chaining** (derive all relationships) and **backward chaining** (answer a query with a reasoning trace).

### Practical 6: Bayes Rule and Naive Bayes Classifier
**Aim:** Apply Bayes' theorem and train a Naive Bayes text classifier.
Calculates `P(Spam | "free")` = 80% by hand, then trains `MultinomialNB` on a small spam/ham email dataset using bag-of-words and reports accuracy, confusion matrix and classification report.

### Practical 7: Linear Regression and Decision Tree
**Aim:** Build a regression model and a decision tree classifier.
Linear Regression predicts house prices from size (price of 1700 sqft ≈ 80.43 Lakh). A Decision Tree (`max_depth=3`) predicts loan approval and prints its rules.

### Practical 8: K-Means Clustering
**Aim:** Group stores into segments and choose the best number of clusters.
Standardises the data, uses the **Elbow Method** for k = 1 to 7, picks k = 3, converts the centroids back to original units and summarises each segment.

### Practical 9: Basic Natural Language Processing
**Aim:** Preprocess text and train a sentiment classifier.
Covers tokenization, stop-word removal and simple stemming, then TF-IDF features and a Naive Bayes classifier that predicts positive or negative sentiment of reviews.

### Practical 10: Mini AI Project – Customer Support Chatbot
**Aim:** Build a complete small AI application.
A rule-based chatbot recognises greetings, order tracking, return policy and store-hours questions using substring pattern matching, with a fallback reply for unknown questions. The file also summarises the problem, approach, limitations and future work.

## Sample Outputs

The saved output of every program is in the [`outputs/`](outputs/) folder, for example [`practical_03_output.txt`](outputs/practical_03_output.txt).

Version numbers (Practical 1) and the order of cluster numbers (Practical 8) can differ slightly on your computer. That is normal.

## Original Journal

The original journal is included here: [`docs/YASH_AGRE_AI_MANUAL.pdf`](docs/YASH_AGRE_AI_MANUAL.pdf)

---

*Prepared for academic purposes as part of the B.Sc. Business AI curriculum, Dr. Homi Bhabha State University.*
