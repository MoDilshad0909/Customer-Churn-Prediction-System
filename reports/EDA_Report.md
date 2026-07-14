# Customer Churn Prediction System - EDA Report

## 1. Project Title
**Customer Churn Prediction & Retention Intelligence Platform** - Exploratory Data Analysis (EDA)

## 2. Dataset Summary
The dataset used is the Telco Customer Churn dataset, representing a fictional telecommunications company that provided home phone and internet services to 7043 customers in California in Q3. The cleaned dataset removes identifiable markers (like CustomerID) and handles initial missing data in numerical columns. It comprises multiple features across categories such as demographics, services, account information, and churn status. 

## 3. Missing Value Analysis
Initial exploration identified that the `Total Charges` column contained some missing values (represented as spaces). These were coerced to NaN and subsequently dropped, leading to a perfectly clean dataset with no further null values. Duplicate rows were also verified and addressed, ensuring robust data quality.

## 4. Target Variable Analysis
The primary target variable is `Churn Label` (or `Churn Value`). The dataset exhibits a significant class imbalance, with a notable portion of customers (~26.5%) churning. This imbalance implies that future predictive modeling may require specialized handling (e.g., SMOTE, class weighting) to achieve optimal recall for churn cases.

## 5. Feature Analysis
The feature set can be divided into three primary categories:
- **Demographics:** `Gender`, `Senior Citizen`, `Partner`, `Dependents`
- **Services:** `Phone Service`, `Multiple Lines`, `Internet Service`, `Online Security`, `Tech Support`, `Streaming TV`, `Streaming Movies`
- **Account Information:** `Contract`, `Paperless Billing`, `Payment Method`, `Monthly Charges`, `Total Charges`, `Tenure Months`

Visualizations highlight that demographic traits like lack of a partner/dependents and being a senior citizen correlate with higher churn. Furthermore, certain services (Fiber optic internet, lack of Tech Support) and account factors (month-to-month contracts, electronic check payments, high monthly charges, low tenure) act as strong predictors for churn.

## 6. Business Insights
1. **Contract Type is Crucial:** Month-to-month contracts are highly susceptible to churn. Customers tied to one-year or two-year contracts show substantially higher retention.
2. **Early Churn Risk:** The first few months of tenure represent a critical 'danger zone.' Most churn occurs within the first 12 months.
3. **Price Sensitivity:** Higher monthly charges, specifically in the $70-$100 range, correlate with higher churn rates, especially among newer customers.
4. **Service Dissatisfaction:** Fiber optic customers are churning at higher rates than DSL customers. Conversely, customers with additional services like Tech Support and Online Security exhibit more loyalty.
5. **Payment Friction:** Customers paying via Electronic Check churn significantly more than those using automated payment systems (Credit Card/Bank Transfer).
6. **Demographic Indicators:** Senior citizens and customers without partners/dependents are more flight-prone.

## 7. Recommendations
- **Incentivize Long-term Contracts:** Offer promotions or discounts to encourage month-to-month customers to switch to 1-year or 2-year contracts.
- **Improve Onboarding:** Implement robust onboarding and early engagement programs specifically targeting customers in their first 1-12 months.
- **Service Bundling:** Provide discounts or targeted bundles that include Tech Support and Online Security, as these sticky services reduce churn.
- **Review Fiber Optic Offering:** Investigate the root cause behind Fiber optic churn—be it pricing, performance, or competitor offerings.
- **Promote Auto-Pay:** Encourage customers to enroll in automatic payments by offering a small monthly discount.

## 8. Conclusion
The Exploratory Data Analysis reveals strong patterns differentiating loyal customers from those likely to churn. The insights generated from these features establish a robust foundation for building predictive machine learning models in the next phase of the project. By addressing the identified risk factors, the business can proactively target at-risk customers and deploy effective retention strategies.
