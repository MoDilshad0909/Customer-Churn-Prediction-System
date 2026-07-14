# 📖 User Guide: Customer Churn Prediction & Retention Intelligence

Welcome to the User Guide for the Customer Churn Prediction platform. This document explains how to navigate the interface and interpret the outputs to make data-driven retention decisions.

## 🧭 Navigation

The application uses a persistent sidebar menu for easy navigation:
1. **Home**: High-level overview of the platform capabilities.
2. **Dashboard**: Executive metrics covering total customers analyzed, model accuracy, and key performance indicators (KPIs).
3. **Predict**: The core predictive engine. Enter customer details here to assess their churn risk.
4. **Analytics**: Deep dive into your customer base through interactive, filterable Plotly charts.
5. **Reports**: Download your AI predictions as PDF or CSV files for offline sharing or auditing.
6. **About**: Metadata, technical architecture, and author contact information.

## 🔮 Making a Prediction

To predict whether a specific customer will churn:
1. Click on **Predict** in the sidebar.
2. Fill out the comprehensive form spanning four categories:
   - **Customer Information**: Demographics like Gender, Senior Citizen status, Partners, and Dependents.
   - **Service Information**: Selected services (e.g., Fiber optic, Tech Support, Streaming TV).
   - **Billing & Contract**: Contract length, Paperless Billing preference, Payment Method, and Monthly/Total Charges.
3. Click the **"Predict Customer Risk"** button.

## 🧠 Understanding the Results

After clicking the predict button, three dynamic sections will appear below the form:

### 1. Prediction Result Badge
- **Customer Will Stay ✅ (Low Risk)**: Probability < 30%. Customer is loyal.
- **Customer is at Risk ⚠️ (Medium Risk)**: Probability between 30% and 50%. Customer shows signs of dissatisfaction.
- **Customer Will Churn 🚨 (High Risk)**: Probability > 50%. Customer is actively preparing to leave.

### 2. Explainable AI (SHAP)
A horizontal bar chart visually breaks down **why** the model made its decision:
- **Red Bars** (pointing right): Factors pushing the customer *towards* churning (e.g., High Monthly Charges, Month-to-Month Contract).
- **Green Bars** (pointing left): Factors pulling the customer *towards* staying (e.g., Having Tech Support, 2-Year Contract).

### 3. AI Insights & Recommendations
Our AI Business Advisor translates the raw prediction and SHAP values into actionable English:
- It highlights the absolute primary risk factor and retention factor.
- It suggests specific business actions (e.g., "Offer a 15% discount", "Enroll in a retention campaign") tailored precisely to the inputs you provided.

## 📄 Generating Reports

If you need to share a prediction with your retention team:
1. Complete a prediction on the **Predict** page.
2. Navigate to the **Reports** page.
3. Click **"Download Prediction Report (PDF)"** to get a formatted summary of the customer's profile, risk level, and AI recommendations.
4. Alternatively, download the data directly to **CSV** for Excel integration.
