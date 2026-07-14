import joblib
import pandas as pd
import numpy as np
import re
from utils.preprocessing import engineer_features
import os

# Define global caches for model and preprocessor to avoid reloading
_PREPROCESSOR = None
_MODEL = None

def load_models():
    """Loads the preprocessor and best model into memory."""
    global _PREPROCESSOR, _MODEL
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    prep_path = os.path.join(base_dir, 'models', 'preprocessor.pkl')
    model_path = os.path.join(base_dir, 'models', 'best_model.pkl')
    
    if _PREPROCESSOR is None:
        _PREPROCESSOR = joblib.load(prep_path)
    if _MODEL is None:
        _MODEL = joblib.load(model_path)
        
    return _PREPROCESSOR, _MODEL

def predict_churn(input_data):
    """
    Takes a dictionary of input features, processes it through the pipeline,
    and returns the churn probability.
    """
    preprocessor, model = load_models()
    
    # 1. Convert to DataFrame
    # Provide default values for fields not in the form but present in training
    defaults = {
        'Count': 1, 'Country': 'United States', 'State': 'California', 'City': 'Los Angeles',
        'Zip Code': 90001, 'Lat Long': '33.973, -118.244', 'Latitude': 33.973, 'Longitude': -118.244,
        'Churn Label': 'No', 'Churn Value': 0, 'Churn Score': 50, 'CLTV': 5000, 'Churn Reason': ''
    }
    
    # Merge defaults with user input
    full_data = {**defaults, **input_data}
    df = pd.DataFrame([full_data])
    
    # 2. Engineer Features
    df = engineer_features(df)
    
    # 3. Drop target columns that were dropped during training
    cols_to_drop = ['Churn Label', 'Churn Value', 'Churn Score', 'CLTV', 'Churn Reason']
    for col in cols_to_drop:
        if col in df.columns:
            df = df.drop(columns=[col])
            
    # 4. Transform Dataset
    transformed_data = preprocessor.transform(df)
    
    # 5. Sanitize feature names if they were sanitized during training
    cat_features = preprocessor.transformers_[1][2]
    new_cols = preprocessor.get_feature_names_out()
    new_cols = [re.sub(r'[\[\]<>{}:",]', '', col) for col in new_cols]
    
    X = pd.DataFrame(transformed_data, columns=new_cols)
    
    # 6. Predict Probability
    probability = model.predict_proba(X)[0][1]
    
    return probability

def generate_ai_insights(probability, input_data):
    """
    Generates automated business advice based on prediction.
    """
    insights = []
    
    if probability > 0.5:
        insights.append("🔴 **High Risk Detected**: The model strongly indicates this customer will churn.")
        if input_data.get('Contract') == 'Month-to-month':
            insights.append("💡 **Recommendation**: Offer a 15% discount for upgrading to a 1-year contract.")
        if float(input_data.get('Monthly Charges', 0)) > 70:
            insights.append("💡 **Recommendation**: This customer has high monthly charges. Consider offering a tailored loyalty package to increase perceived value.")
        if input_data.get('Tech Support') == 'No':
            insights.append("💡 **Recommendation**: Provide a free month of Tech Support to improve their service experience.")
    elif probability > 0.3:
        insights.append("🟡 **Moderate Risk**: Monitor this customer closely.")
        if input_data.get('Payment Method') == 'Electronic check':
            insights.append("💡 **Recommendation**: Incentivize them to switch to automatic payments (e.g., Credit Card) to reduce payment friction.")
        insights.append("💡 **Recommendation**: Enroll them in a proactive retention campaign with a courtesy check-in call.")
    else:
        insights.append("🟢 **Low Risk**: This customer exhibits strong loyalty indicators.")
        insights.append("💡 **Recommendation**: Ideal candidate for cross-selling premium add-ons or referral programs.")
        if input_data.get('Internet Service') == 'Fiber optic':
            insights.append("💡 **Recommendation**: Suggest premium streaming packages to maximize their high-speed connection.")
            
    return insights
