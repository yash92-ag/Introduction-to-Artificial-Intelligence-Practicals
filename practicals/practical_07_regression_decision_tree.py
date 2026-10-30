"""
Practical 7: Linear Regression and Decision Tree

Aim:
    To build and evaluate a Linear Regression model on housing price data
    and a Decision Tree classifier on credit loan approval data.

How to run:
    python practicals/practical_07_regression_decision_tree.py
"""

import pandas as pd

# ---------------------------------------------------------------
# PART 1: Linear Regression (predicting house prices)
# ---------------------------------------------------------------
from sklearn.linear_model import LinearRegression

# Housing dataset: size in square feet and price in Lakh
housing = pd.DataFrame({
    "HouseSize_sqft": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Price_Lakh": [40, 48, 58, 70, 85, 95, 102, 118]
})

X = housing[["HouseSize_sqft"]]   # input (double brackets keep it as a table)
y = housing["Price_Lakh"]         # output we want to predict

reg_model = LinearRegression()
reg_model.fit(X, y)               # the model learns the best straight line

intercept = reg_model.intercept_
slope = reg_model.coef_[0]
r_squared = reg_model.score(X, y) # closer to 1 means a better fit

print(f"Regression Equation: Price = {slope:.4f} * HouseSize + {intercept:.4f}")
print(f"R² Score: {r_squared:.4f}")

# Valuation for a 1700 sqft apartment
pred_1700 = reg_model.predict(pd.DataFrame({"HouseSize_sqft": [1700]}))[0]
print(f"Predicted price for 1700 sqft: {pred_1700:.2f} Lakh")

# ---------------------------------------------------------------
# PART 2: Decision Tree (loan approval)
# ---------------------------------------------------------------
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

loan = pd.DataFrame({
    "Income": [35000, 60000, 28000, 75000, 42000, 25000, 90000, 32000],
    "CreditScore": [650, 720, 600, 750, 680, 580, 780, 610],
    "Employed": [1, 1, 0, 1, 1, 0, 1, 0],   # 1 = Yes, 0 = No
    "LoanApproved": ["No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No"]
})

X_loan = loan[["Income", "CreditScore", "Employed"]]
y_loan = loan["LoanApproved"]

# Keep 25% of the data aside for testing
X_train, X_test, y_train, y_test = train_test_split(
    X_loan, y_loan, test_size=0.25, random_state=42)

# max_depth=3 stops the tree from growing too big
tree_model = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_model.fit(X_train, y_train)

y_pred = tree_model.predict(X_test)
print(f"Decision Tree Test Accuracy: {accuracy_score(y_test, y_pred) * 100:.1f}%")

# Print the rules the tree learned
print("\nDecision Tree Rules:\n",
      export_text(tree_model, feature_names=["Income", "CreditScore", "Employed"]))
