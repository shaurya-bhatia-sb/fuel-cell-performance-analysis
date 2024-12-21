
# Fuel Cell Performance Analysis

## Overview
This project analyzes fuel cell performance data using various regression models. The dataset is split based on roll number logic, and model performance is evaluated with metrics like Mean Squared Error (MSE) and R² Score.

## Dataset
The dataset `Fuel_cell_performance_data-Full.csv` should be placed in the `data/` directory.

## Features
- Roll number-based target column selection.
- Data preprocessing to handle missing values.
- Multiple regression models:
  - Linear Regression
  - Decision Tree
  - Random Forest
  - Gradient Boosting
  - Support Vector Regressor
  - K-Neighbors Regressor
  - AdaBoost Regressor
  - Hist Gradient Boosting Regressor
  - XGBoost Regressor
  - CatBoost Regressor
    
## Requirements
- Python 3.8+
- Required Libraries:
  - pandas
  - scikit-learn
  - xgboost
  - catboost

## Results
The results are displayed in the console after executing the script.
Model performance is evaluated using the following metrics:
 - **Mean Squared Error (MSE)**
 - **R² Score**
   
![Results](results/results.png)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fuel-cell-performance-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fuel-cell-performance-analysis
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the analysis script:
   ```bash
   python src/fuel_cell_analysis.py
   ```

## Project Structure
```
fuel-cell-performance-analysis/
|
├── data/
│   └── Fuel_cell_performance_data-Full.csv  # Dataset
│
├── src/
│   └── fuel_cell_analysis.py  # Main analysis script
│
├── requirements.txt  # Dependencies
├── results/
│   └── results.png  # screenshot of model evaluations
├── README.md         # Project documentation

```



## License
This project is licensed under the MIT License.


## Contributing
If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.


---
  
Made with ❤️ by Shaurya Bhatia
