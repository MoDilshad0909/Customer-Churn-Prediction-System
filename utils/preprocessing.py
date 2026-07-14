import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def load_dataset(filepath):
    """
    Load dataset from a given filepath.
    """
    df = pd.read_csv(filepath)
    return df

def engineer_features(df):
    """
    Perform feature engineering.
    - TotalCharges numeric conversion (handled if string, but already handled in Day 1, still safe to apply)
    - tenure groups
    - MonthlyCharges categories
    - TotalCharges categories
    - Contract length features
    """
    # 1. TotalCharges numeric conversion
    if 'Total Charges' in df.columns:
        df['Total Charges'] = pd.to_numeric(df['Total Charges'].replace(' ', np.nan), errors='coerce')
        df['Total Charges'] = df['Total Charges'].fillna(0) # or drop, but filling is safer here
        
    # 2. Tenure groups
    if 'Tenure Months' in df.columns:
        bins = [0, 12, 24, 36, 48, 60, 72, 100]
        labels = ['0-12', '13-24', '25-36', '37-48', '49-60', '61-72', '73+']
        df['Tenure Group'] = pd.cut(df['Tenure Months'], bins=bins, labels=labels, right=False).astype(str)
        
    # 3. MonthlyCharges categories
    if 'Monthly Charges' in df.columns:
        charge_bins = [0, 30, 60, 90, 150]
        charge_labels = ['Low', 'Medium', 'High', 'Premium']
        df['Monthly Charge Group'] = pd.cut(df['Monthly Charges'], bins=charge_bins, labels=charge_labels, right=False).astype(str)

    # 4. TotalCharges categories
    if 'Total Charges' in df.columns:
        tc_bins = [0, 1000, 3000, 5000, 10000]
        tc_labels = ['Low', 'Medium', 'High', 'Very High']
        df['Total Charge Group'] = pd.cut(df['Total Charges'], bins=tc_bins, labels=tc_labels, right=False).astype(str)

    # 5. Contract length features
    if 'Contract' in df.columns:
        # Mapping contract length to numerical months approximation
        contract_map = {'Month-to-month': 1, 'One year': 12, 'Two year': 24}
        df['Contract Length (Months)'] = df['Contract'].map(contract_map).fillna(1)
        
    return df

def split_dataset(df, target_col='Churn Label', test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets, stratifying on the target.
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

def build_preprocessor(numeric_features, categorical_features):
    """
    Build the preprocessing pipeline using ColumnTransformer.
    """
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ],
        remainder='drop' # Drops any columns not explicitly defined in features
    )
    
    return preprocessor

def transform_dataset(preprocessor, X_train, X_test):
    """
    Fit the preprocessor on X_train and transform both X_train and X_test.
    """
    # Fit and transform training data
    X_train_transformed = preprocessor.fit_transform(X_train)
    # Get column names after transformation
    cat_features = preprocessor.transformers_[1][2]
    # In scikit-learn 1.2+, get_feature_names_out can be used
    new_cols = preprocessor.get_feature_names_out()
    
    X_train_df = pd.DataFrame(X_train_transformed, columns=new_cols, index=X_train.index)
    
    # Transform test data
    X_test_transformed = preprocessor.transform(X_test)
    X_test_df = pd.DataFrame(X_test_transformed, columns=new_cols, index=X_test.index)
    
    return X_train_df, X_test_df, preprocessor

def save_pipeline(pipeline, filepath):
    """
    Save the trained pipeline to disk using joblib.
    """
    joblib.dump(pipeline, filepath)
    print(f"Pipeline saved to {filepath}")
