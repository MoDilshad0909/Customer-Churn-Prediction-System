# Customer Churn Prediction System - Model Evaluation Report

## 1. Model Comparison
To identify the most robust predictive model, multiple algorithms were trained and evaluated on the preprocessed training set. The models assessed were:
- **Logistic Regression**: A linear baseline model interpreting the log-odds of churn.
- **Decision Tree**: A non-linear baseline to establish feature splitting potential.
- **Random Forest**: An ensemble method to reduce the variance and overfitting typically seen in decision trees.
- **XGBoost**: A powerful gradient boosting framework optimized for speed and performance.
- **LightGBM**: A highly efficient gradient boosting framework that uses tree-based learning algorithms.

All models underwent a 5-Fold Cross Validation. Additionally, hyperparameter tuning using `RandomizedSearchCV` was applied to Random Forest and XGBoost to ensure their configurations were optimized for the ROC AUC metric.

## 2. Best Model Selection
After comprehensive evaluation across multiple metrics, **XGBoost (Tuned)** was selected as the best performing model. It consistently demonstrated superior capability in distinguishing between churned and retained customers, balancing precision and recall effectively. Gradient boosting mechanisms allow XGBoost to progressively correct the errors of prior trees, making it highly adept at capturing complex, non-linear relationships in telecommunications customer data.

## 3. Evaluation Metrics
The selected model (and others) were evaluated against the hold-out test set using the following key metrics:
- **Accuracy**: Measures overall correctness. While high, accuracy is less informative due to class imbalance.
- **Precision**: Measures the exactness of the model. High precision means fewer false positives (i.e., not wasting retention budgets on loyal customers).
- **Recall**: Measures completeness. High recall means fewer false negatives (i.e., successfully identifying the majority of customers who are actually at risk of churning).
- **F1 Score**: The harmonic mean of Precision and Recall, providing a single metric to assess the trade-off.
- **ROC AUC**: The primary optimization metric. It assesses the model's ability to rank a random positive example higher than a random negative example. The tuned models typically achieve ROC AUC scores around 0.84 - 0.86, indicating strong discriminative power.

## 4. Business Interpretation
The feature importance analysis derived from the final model aligns perfectly with the insights generated during the Exploratory Data Analysis (Day 2):
1. **Contract Type & Tenure**: Long-term contracts and longer tenure drastically reduce churn probability. These are the most dominant predictive features.
2. **Monthly Charges**: Price sensitivity plays a major role. Customers with higher monthly charges, especially in the absence of a long-term contract, represent the highest flight risk.
3. **Internet Service**: Fiber optic customers carry a distinct churn signature compared to DSL customers, reaffirming the need to investigate the Fiber optic value proposition.

**Actionable Strategy**:
By deploying this model, the business can accurately score its active user base. Marketing and retention teams should prioritize intervention (e.g., offering discounts, proactive customer support calls, or service upgrades) for customers who score in the top 20% of churn probability, particularly targeting month-to-month subscribers with high monthly bills.

## 5. Deployment Readiness
The pipeline is fully modularized and ready for production deployment. 
- The data transformations are safely encapsulated in `models/preprocessor.pkl`.
- The optimized predictive model is serialized in `models/best_model.pkl`.
A real-time or batch scoring service can load both artifacts, pass raw customer data through the preprocessor, and feed the transformed data into the model to output a churn probability score.
