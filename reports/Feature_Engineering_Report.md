# Customer Churn Prediction System - Feature Engineering Report

## 1. Project Summary
This report summarizes the feature engineering and preprocessing steps applied to the Telco Customer Churn dataset. Following the exploratory data analysis (EDA), the dataset required structuring and transformation to make it suitable for training machine learning models. A robust, reproducible pipeline was developed to automate these transformations, ensuring production-quality standards and avoiding data leakage.

## 2. Features Created
To extract more predictive signal from the raw data, the following features were engineered:
- **Total Charges Numeric Conversion:** Ensured the `Total Charges` column was strictly numeric, coercing any whitespace to `NaN` and handling missing values appropriately.
- **Tenure Group:** Binned the continuous `Tenure Months` feature into logical categories (e.g., '0-12', '13-24', '25-36' months) to capture distinct customer lifecycle stages.
- **Monthly Charge Group:** Binned `Monthly Charges` into 'Low', 'Medium', 'High', and 'Premium' categories to account for varying price sensitivity thresholds.
- **Total Charge Group:** Categorized accumulated `Total Charges` into grouped brackets.
- **Contract Length (Months):** Converted the categorical `Contract` types ('Month-to-month', 'One year', 'Two year') into an approximate numerical representation of duration in months (1, 12, 24).

## 3. Encoding Method
Categorical variables (e.g., Demographics, Services, and our newly engineered categorical groups) were automatically detected. We applied **OneHotEncoder** with `handle_unknown='ignore'` and `sparse_output=False`. This strategy ensures that non-ordinal categorical data is properly binarized for machine learning algorithms without imposing arbitrary ordinality, and it safely handles any unseen categories in future predictions.

## 4. Scaling Method
Numerical features were automatically isolated and scaled using **StandardScaler**. This transformation standardizes the numerical data to have a mean of 0 and a standard deviation of 1. Scaling is crucial for ensuring that features with larger magnitudes (like `Total Charges`) do not disproportionately influence distance-based algorithms or gradient descent convergence.

## 5. Train Test Split
The dataset was split into training and testing sets with the following configuration:
- **Ratio:** 80% Training / 20% Testing
- **Random State:** 42 (for reproducibility)
- **Stratification:** Applied using the target variable (`Churn Label`). This guarantees that the original class imbalance is accurately reflected in both the training and testing sets, preventing biased evaluation metrics.

## 6. Pipeline Design
The preprocessing workflow was unified using scikit-learn's `ColumnTransformer` and `Pipeline` architectures. 
- A numeric pipeline handles the application of `StandardScaler`.
- A categorical pipeline handles the `OneHotEncoder`.
By wrapping these in a single `ColumnTransformer`, we created a cohesive, reusable object that can fit on training data and subsequently transform validation/test data or real-time production inference data without risking data leakage.

## 7. Files Generated
The execution of the feature engineering notebook successfully generated the following artifacts:
- **`models/preprocessor.pkl`**: The fitted scikit-learn `ColumnTransformer` pipeline, saved via Joblib for future deployment.
- **`dataset/X_train.csv`**: The fully preprocessed and transformed feature set for model training.
- **`dataset/X_test.csv`**: The fully preprocessed and transformed feature set for model evaluation.
- **`dataset/y_train.csv`**: The training target variables.
- **`dataset/y_test.csv`**: The testing target variables.

## 8. Conclusion
The feature engineering and preprocessing pipeline establishes a clean, mathematically sound foundation for predictive modeling. By isolating the preprocessing steps into a reusable pipeline and extracting additional insights through feature engineering, the project is now ready for Day 4: Model Training and Evaluation.
