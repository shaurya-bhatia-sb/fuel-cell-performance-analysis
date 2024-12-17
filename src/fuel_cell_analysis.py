import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, HistGradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv("data/Fuel_cell_performance_data-Full.csv")

# Replace 'Your_Roll_Number' with your roll number
roll_number = "102203519"  # Example Roll Number
last_digit = int(roll_number[-1])

# Determine target column based on the last digit of roll number
if last_digit in [0, 5]:
    target_column = "Target1"
elif last_digit in [1, 6]:
    target_column = "Target2"
elif last_digit in [2, 7]:
    target_column = "Target3"
elif last_digit in [3, 8]:
    target_column = "Target4"
elif last_digit in [4, 9]:
    target_column = "Target5"
else:
    raise ValueError("Invalid roll number.")

# Ensure the target column exists
if target_column not in data.columns:
    raise ValueError(f"{target_column} not found in dataset columns.")

# Select the target column and drop others
data = data.dropna()  # Drop rows with missing values
data = data.drop(columns=[col for col in data.columns if col.startswith("Target") and col != target_column])

# Split dataset into features and target
X = data.drop(columns=[target_column])
y = data[target_column]

# Split the dataset into 70% training and 30% testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
    "Support Vector Regressor": SVR(),
    "K-Neighbors Regressor": KNeighborsRegressor(),
    "AdaBoost Regressor": AdaBoostRegressor(random_state=42),
    "Hist Gradient Boosting": HistGradientBoostingRegressor(random_state=42),
    "XGBoost Regressor": XGBRegressor(random_state=42, verbosity=0),
    "CatBoost Regressor": CatBoostRegressor(verbose=0, random_state=42)
}

# Train and evaluate models
results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[model_name] = {"MSE": mse, "R2 Score": r2}

# Print results
print("\nModel Performance:")
for model_name, metrics in results.items():
    print(f"\n{model_name}")
    for metric, value in metrics.items():
        print(f"{metric}: {value}")
