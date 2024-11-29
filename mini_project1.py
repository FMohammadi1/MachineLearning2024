# -*- coding: utf-8 -*-
"""Mini Project1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1as7UHUXiU6_lP1v1eDwAYoZIb81Sbb7Q
"""

#!/bin/bash
!kaggle datasets download sakshigoyal7/credit-card-customers
!unzip credit-card-customers.zip

import pandas as pd

# Load dataset
df = pd.read_csv('/content/BankChurners.csv')

print(df.info())
print(df.head())


# Display the columns of the dataset (features)
print("Features (Columns) in the dataset:")
print(df.columns.tolist())

# Number of samples
num_samples = df.shape[0]
print(f'تعداد نمونه‌های موجود در مجموعه داده: {num_samples}')


print(df.Total_Trans_Ct[2],df.Total_Trans_Ct.unique(),df.Total_Trans_Ct.value_counts())

import seaborn as sns
import matplotlib.pyplot as plt


selected_features = ['Customer_Age', 'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1']

# Pairplot for the selected features
sns.pairplot(df[selected_features])
plt.show()

# Select categorical and continuous features
categorical_features = ['Gender', 'Attrition_Flag']
continuous_features = ['Customer_Age', 'Credit_Limit']

# Convert categorical features to numeric values
df_encoded = pd.get_dummies(df[categorical_features], drop_first=True)

# Combine continuous and encoded categorical features
df_combined = pd.concat([df[continuous_features], df_encoded], axis=1)

# Compute the correlation matrix
correlation_matrix = df_combined.corr()

# Display the heatmap of correlations
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap of Correlation between Selected Features')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# Importing the matplotlib.pyplot module

# Calculate correlation matrix, only including numerical features
correlation_matrix = df.select_dtypes(include=['number']).corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.show()

df.isna()
print(df.shape)
df.isna().any()
df.dropna(axis=0, inplace=True)
print(df.shape)

import pandas as pd

# Check if there are missing values (NaN) in the dataset
print(df.isnull().sum())

# Optionally, check for rows with missing values
print(df[df.isnull().any(axis=1)])

# If there are NaN values, you can either drop them or fill them
# Dropping rows with NaN values
df_cleaned = df.dropna()



# Alternatively, filling NaN values with a specific value (mean, median, etc.)
# Select only numeric columns for filling with mean
numeric_cols = df.select_dtypes(include=['number']).columns
df_filled = df.copy()  # Create a copy to avoid modifying the original DataFrame
df_filled[numeric_cols] = df_filled[numeric_cols].fillna(df_filled[numeric_cols].mean())

# Check the unique classes in the 'Attrition_Flag' feature
print(df['Attrition_Flag'].value_counts())

# Display a pie chart for the distribution of the 'Attrition_Flag' feature
plt.figure(figsize=(6, 6))
df['Attrition_Flag'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Attrition Flag')
plt.ylabel('')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Prepare data
X = df.drop(['Attrition_Flag'], axis=1)
y = df['Attrition_Flag']

# Convert categorical features to dummy variables
X = pd.get_dummies(X, drop_first=True)


# Split data
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Train model without balancing
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


# Evaluate model
y_train_pred = model.predict(X_train)
y_val_pred = model.predict(X_val)
print('Training Classification Report:')
print(classification_report(y_train, y_train_pred))
print('Validation Classification Report:')
print(classification_report(y_val, y_val_pred))
print('Validation Confusion Matrix:')
print(confusion_matrix(y_val, y_val_pred))

from imblearn.over_sampling import SMOTE

# Apply SMOTE to balance training data
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Train model with balanced data
model_balanced = RandomForestClassifier(random_state=42)
model_balanced.fit(X_train_resampled, y_train_resampled)

# Evaluate balanced model
y_train_resampled_pred = model_balanced.predict(X_train_resampled)
y_val_balanced_pred = model_balanced.predict(X_val)
print('Balanced Training Classification Report:')
print(classification_report(y_train_resampled, y_train_resampled_pred))
print('Balanced Validation Classification Report:')
print(classification_report(y_val, y_val_balanced_pred))
print('Balanced Validation Confusion Matrix:')
print(confusion_matrix(y_val, y_val_balanced_pred))

import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the actual column name is 'Attrition_Flag'
sns.pairplot(df, hue='Attrition_Flag', vars=['Customer_Age', 'Credit_Limit', 'Total_Trans_Amt', 'Total_Trans_Ct'])
plt.show()

"""پرسش دوم"""

!pip install --upggrade --no-cache-dir gdown
!gdown 1PeQVXfT-aYBH0V1mn7ovo6yp3fq7WjdK

import numpy as np
import pandas as pd

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)
df = pd.DataFrame(data)
print(df.info())
print(df.head())

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)

# Create x values based on the length of data
x = np.linspace(-5, 12, len(data))

# Combine x and y into a DataFrame
df = pd.DataFrame({'x': x, 'y': data})
print(df.info())
print(df.head())

# Split the data into features (X) and target (y)
X = df[['x']]
y = df['y']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Plot the training and testing data
plt.figure(figsize=(12, 6))
plt.plot(X_train, y_train, 'o', label='Training Data')
plt.plot(X_test, y_test, 'x', label='Testing Data')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Training and Testing Data Distribution')
plt.show()

# Train a Linear Regression model and plot error curves
train_errors, test_errors = [], []

model = LinearRegression()

for m in range(1, len(X_train)):
    model.fit(X_train[:m], y_train[:m])
    y_train_predict = model.predict(X_train[:m])
    y_test_predict = model.predict(X_test)

    train_errors.append(mean_squared_error(y_train[:m], y_train_predict))
    test_errors.append(mean_squared_error(y_test, y_test_predict))

# Plotting the error curves
plt.figure(figsize=(12, 6))
plt.plot(np.sqrt(train_errors), 'r-+', linewidth=2, label='Training Error')
plt.plot(np.sqrt(test_errors), 'b-', linewidth=3, label='Testing Error')
plt.legend()
plt.xlabel('Training Set Size')
plt.ylabel('RMSE')
plt.title('Learning Curves')
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression


# Evaluate the final model
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R² Score: {r2}')

import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)

# Create x values based on the length of data
x = np.linspace(-5, 12, len(data))
y = data

# Number of data points
n = len(x)

# Calculate sums
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x_squared = np.sum(x ** 2)

# Calculate slope (m) and intercept (b)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
b = np.mean(y) - m * np.mean(x)

# Display the calculated slope and intercept
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Make predictions
y_pred = m * x + b

# Plot the original data and the fitted line
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()

# Calculate Mean Squared Error (MSE) for evaluation
mse = np.mean((y - y_pred) ** 2)
print(f'Mean Squared Error (MSE): {mse}')

"""Q2.4"""

import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)

# Create x values based on the length of data
x = np.linspace(-5, 12, len(data))
y = data

# Split data into training and testing sets
split_ratio = 0.8
split_index = int(split_ratio * len(x))

x_train = x[:split_index]
y_train = y[:split_index]
x_test = x[split_index:]
y_test = y[split_index:]

# Initialize lists to store errors
train_errors = []
test_errors = []

# Iterative training
for i in range(1, len(x_train) + 1):
    # Select first i samples for training
    x_train_subset = x_train[:i]
    y_train_subset = y_train[:i]

    # Calculate sums for least squares method
    n = len(x_train_subset)
    sum_x = np.sum(x_train_subset)
    sum_y = np.sum(y_train_subset)
    sum_xy = np.sum(x_train_subset * y_train_subset)
    sum_x_squared = np.sum(x_train_subset ** 2)

    # Calculate slope (m) and intercept (b)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    b = np.mean(y_train_subset) - m * np.mean(x_train_subset)

    # Make predictions
    y_train_pred = m * x_train_subset + b
    y_test_pred = m * x_test + b

    # Calculate Mean Squared Error (MSE)
    train_mse = np.mean((y_train_subset - y_train_pred) ** 2)
    test_mse = np.mean((y_test - y_test_pred) ** 2)

    # Store errors
    train_errors.append(train_mse)
    test_errors.append(test_mse)

# Plot the training and test errors
plt.figure(figsize=(12, 6))
plt.plot(range(1, len(x_train) + 1), train_errors, label='Train Error')
plt.plot(range(1, len(x_train) + 1), test_errors, label='Test Error')
plt.xlabel('Number of Training Samples')
plt.ylabel('Mean Squared Error (MSE)')
plt.title('Train and Test Errors vs. Number of Training Samples')
plt.legend()
plt.show()

"""Q2.6"""

import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)
x = np.linspace(-5, 12, len(data))
y = data
X = x.reshape(-1, 1)  # feature
#y = data[:, 1]  # target

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to add polynomial features
def add_polynomial_features(X, degree):
    X_poly = X
    for d in range(2, degree + 1):
        X_poly = np.hstack((X_poly, X**d))
    return X_poly

# Initialize lists to store errors
train_errors = []
test_errors = []

# Loop through polynomial degrees
max_degree = 5
for degree in range(1, max_degree + 1):
    X_train_poly = add_polynomial_features(X_train, degree)
    X_test_poly = add_polynomial_features(X_test, degree)

    # Train the model on the polynomial features
    theta = np.linalg.inv(X_train_poly.T @ X_train_poly) @ X_train_poly.T @ y_train

    # Predict on the training and test sets
    y_train_predict = X_train_poly @ theta
    y_test_predict = X_test_poly @ theta

    # Calculate training and test errors
    train_error = np.mean((y_train - y_train_predict) ** 2)
    test_error = np.mean((y_test - y_test_predict) ** 2)

    train_errors.append(train_error)
    test_errors.append(test_error)

# Plot training and test errors
plt.figure(figsize=(10, 6))
plt.plot(range(1, max_degree + 1), train_errors, label="Training Error")
plt.plot(range(1, max_degree + 1), test_errors, label="Test Error")
plt.xlabel("Polynomial Degree")
plt.ylabel("Mean Squared Error")
plt.title("Training and Test Error vs. Polynomial Degree")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)
x = np.linspace(-5, 12, len(data))
y = data
X = x.reshape(-1, 1)  # feature

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Function to add polynomial features
def add_polynomial_features(X, degree):
    X_poly = X
    for d in range(2, degree + 1):
        X_poly = np.hstack((X_poly, X**d))
    return X_poly

# Initialize lists to store errors
train_errors = []
test_errors = []

# Loop through polynomial degrees
max_degree = 5
best_degree = 1
min_test_error = float('inf')

for degree in range(1, max_degree + 1):
    X_train_poly = add_polynomial_features(X_train, degree)
    X_test_poly = add_polynomial_features(X_test, degree)

    # Train the model on the polynomial features
    theta = np.linalg.inv(X_train_poly.T @ X_train_poly) @ X_train_poly.T @ y_train

    # Predict on the training and test sets
    y_train_predict = X_train_poly @ theta
    y_test_predict = X_test_poly @ theta

    # Calculate training and test errors
    train_error = np.mean((y_train - y_train_predict) ** 2)
    test_error = np.mean((y_test - y_test_predict) ** 2)

    train_errors.append(train_error)
    test_errors.append(test_error)

    # Keep track of the degree with the smallest test error
    if test_error < min_test_error:
        min_test_error = test_error
        best_degree = degree

# Now train the best model with the optimal degree
X_train_poly = add_polynomial_features(X_train, best_degree)
X_test_poly = add_polynomial_features(X_test, best_degree)

theta = np.linalg.inv(X_train_poly.T @ X_train_poly) @ X_train_poly.T @ y_train

# Predict on the training and test sets using the best model
y_train_predict = X_train_poly @ theta
y_test_predict = X_test_poly @ theta

# Plot the model's prediction and the original data for the final model (best degree)
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")
plt.plot(X_train, y_train_predict, color="red", label=f"Model Prediction (Degree {best_degree})")
plt.xlabel("X")
plt.ylabel("y")
plt.title(f"Model Prediction vs Original Data (Degree {best_degree})")
plt.legend()
plt.show()

"""Q2.7"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)
x = np.linspace(-5, 12, len(data))
y = data
X = x.reshape(-1, 1)  # feature

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
linear_model = LinearRegression()
ridge_model = Ridge(alpha=1.0)  # Regularization strength for Ridge
lasso_model = Lasso(alpha=0.1)  # Regularization strength for Lasso

# Train models
linear_model.fit(X_train, y_train)
ridge_model.fit(X_train, y_train)
lasso_model.fit(X_train, y_train)

# Predict on the test set
y_train_predict_linear = linear_model.predict(X_train)
y_test_predict_linear = linear_model.predict(X_test)

y_train_predict_ridge = ridge_model.predict(X_train)
y_test_predict_ridge = ridge_model.predict(X_test)

y_train_predict_lasso = lasso_model.predict(X_train)
y_test_predict_lasso = lasso_model.predict(X_test)

# Calculate mean squared error (MSE)
mse_linear_train = mean_squared_error(y_train, y_train_predict_linear)
mse_linear_test = mean_squared_error(y_test, y_test_predict_linear)

mse_ridge_train = mean_squared_error(y_train, y_train_predict_ridge)
mse_ridge_test = mean_squared_error(y_test, y_test_predict_ridge)

mse_lasso_train = mean_squared_error(y_train, y_train_predict_lasso)
mse_lasso_test = mean_squared_error(y_test, y_test_predict_lasso)

# Display results
print("Linear Regression MSE (Train, Test):", mse_linear_train, mse_linear_test)
print("Ridge Regression MSE (Train, Test):", mse_ridge_train, mse_ridge_test)
print("Lasso Regression MSE (Train, Test):", mse_lasso_train, mse_lasso_test)

# Plot predictions vs true values
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")
plt.plot(X, linear_model.predict(X), color="red", label="Linear Model")
plt.plot(X, ridge_model.predict(X), color="orange", label="Ridge Model")
#plt.plot(X, lasso_model.predict(X), color="purple", label="Lasso Model")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Comparison of Linear, Ridge, and Lasso Models")
plt.legend()
plt.show()

"""امتیازی"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Load dataset
data = np.load('/content/data.npy', allow_pickle=True)
x = np.linspace(-5, 12, len(data))
y = data
X = x.reshape(-1, 1)  # feature

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 1. Without Regularization ---

# Linear Regression without regularization
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Predict on the test set
y_train_predict_linear = linear_model.predict(X_train)
y_test_predict_linear = linear_model.predict(X_test)

# Calculate mean squared error (MSE) for linear regression
mse_linear_train = mean_squared_error(y_train, y_train_predict_linear)
mse_linear_test = mean_squared_error(y_test, y_test_predict_linear)

# --- 2. With Regularization (Ridge & Lasso) ---

# Ridge Regression (with regularization)
ridge_model = Ridge(alpha=1.0)  # alpha controls the strength of regularization
ridge_model.fit(X_train, y_train)

# Lasso Regression (with regularization)
lasso_model = Lasso(alpha=0.1)  # alpha controls the strength of regularization
lasso_model.fit(X_train, y_train)

# Predict on the test set
y_train_predict_ridge = ridge_model.predict(X_train)
y_test_predict_ridge = ridge_model.predict(X_test)

y_train_predict_lasso = lasso_model.predict(X_train)
y_test_predict_lasso = lasso_model.predict(X_test)

# Calculate mean squared error (MSE) for Ridge and Lasso
mse_ridge_train = mean_squared_error(y_train, y_train_predict_ridge)
mse_ridge_test = mean_squared_error(y_test, y_test_predict_ridge)

mse_lasso_train = mean_squared_error(y_train, y_train_predict_lasso)
mse_lasso_test = mean_squared_error(y_test, y_test_predict_lasso)

# --- 3. Polynomial Regression with Regularization ---

# Create polynomial features (degree 5)
poly = PolynomialFeatures(degree=5)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train Ridge and Lasso on polynomial features
ridge_poly_model = Ridge(alpha=1.0)
ridge_poly_model.fit(X_train_poly, y_train)

lasso_poly_model = Lasso(alpha=0.1)
lasso_poly_model.fit(X_train_poly, y_train)

# Predict on the test set for polynomial models
y_train_predict_ridge_poly = ridge_poly_model.predict(X_train_poly)
y_test_predict_ridge_poly = ridge_poly_model.predict(X_test_poly)

y_train_predict_lasso_poly = lasso_poly_model.predict(X_train_poly)
y_test_predict_lasso_poly = lasso_poly_model.predict(X_test_poly)

# Calculate mean squared error (MSE) for polynomial models
mse_ridge_poly_train = mean_squared_error(y_train, y_train_predict_ridge_poly)
mse_ridge_poly_test = mean_squared_error(y_test, y_test_predict_ridge_poly)

mse_lasso_poly_train = mean_squared_error(y_train, y_train_predict_lasso_poly)
mse_lasso_poly_test = mean_squared_error(y_test, y_test_predict_lasso_poly)

# Display results
print("Linear Regression MSE (Train, Test):", mse_linear_train, mse_linear_test)
print("Ridge Regression MSE (Train, Test):", mse_ridge_train, mse_ridge_test)
print("Lasso Regression MSE (Train, Test):", mse_lasso_train, mse_lasso_test)

print("Ridge Polynomial MSE (Train, Test):", mse_ridge_poly_train, mse_ridge_poly_test)
print("Lasso Polynomial MSE (Train, Test):", mse_lasso_poly_train, mse_lasso_poly_test)

# Plot predictions vs true values for final models
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color="blue", label="Training Data")
plt.scatter(X_test, y_test, color="green", label="Test Data")

# Plot Linear Model
plt.plot(X, linear_model.predict(X), color="red", label="Linear Model")

# Plot Ridge Model
plt.plot(X, ridge_model.predict(X), color="orange", label="Ridge Model")

# Plot Lasso Model
plt.plot(X, lasso_model.predict(X), color="purple", label="Lasso Model")

# Plot Polynomial Ridge Model
plt.plot(X, ridge_poly_model.predict(poly.transform(X)), color="cyan", label="Ridge Polynomial")

# Plot Polynomial Lasso Model
plt.plot(X, lasso_poly_model.predict(poly.transform(X)), color="magenta", label="Lasso Polynomial")

plt.xlabel("X")
plt.ylabel("y")
plt.title("Comparison of Models (Linear, Ridge, Lasso, Polynomial with Regularization)")
plt.legend()
plt.show()