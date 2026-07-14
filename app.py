import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import json

# Must be the first Streamlit command
st.set_page_config(
    page_title="Churn Prediction & Retention AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

from utils.styles import apply_theme
from utils.components import kpi_card, glass_card, prediction_result_card
from utils.predict import predict_churn, generate_ai_insights
from utils.charts import (
    plot_customer_distribution, 
    plot_contract_distribution, 
    plot_monthly_charges,
    plot_tenure_analysis,
    plot_feature_importance,
    plot_local_shap
)
from utils.helpers import generate_prediction_pdf

# Apply dark premium theme
apply_theme()

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: white;'>Retention AI ✨</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Dashboard", "Predict", "Analytics", "Reports", "About"],
        icons=["house", "speedometer2", "magic", "graph-up", "file-earmark-pdf", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#A855F7", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px", "--hover-color": "rgba(255,255,255,0.05)"},
            "nav-link-selected": {"background-color": "rgba(168, 85, 247, 0.2)", "border-left": "4px solid #A855F7"},
        }
    )
    
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: #64748b; font-size: 0.8rem;'>v1.0.0 Enterprise</div>", unsafe_allow_html=True)

# Initialize session state for prediction results
if 'prediction_made' not in st.session_state:
    st.session_state['prediction_made'] = False
if 'prediction_prob' not in st.session_state:
    st.session_state['prediction_prob'] = 0.0
if 'input_data' not in st.session_state:
    st.session_state['input_data'] = {}
if 'risk_level' not in st.session_state:
    st.session_state['risk_level'] = "Low"
if 'insights' not in st.session_state:
    st.session_state['insights'] = []
if 'shap_df' not in st.session_state:
    st.session_state['shap_df'] = None

# --- PAGE: Home ---
if selected == "Home":
    st.markdown("<h1 style='text-align: center; margin-top: 2rem;'>Customer Churn Prediction &<br>Retention Intelligence Platform</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #cbd5e1; max-width: 800px; margin: 0 auto; margin-bottom: 3rem;'>Predict customer churn using Machine Learning and generate AI-powered retention strategies for your business.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔮 Start Prediction"):
            # Streamlit rerun workaround for sidebar navigation change programmatically is tricky,
            # so we just provide a prompt to click the sidebar.
            st.info("👈 Click on 'Predict' in the sidebar to begin!")
            
    st.markdown("<div style='margin-top: 5rem;'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        glass_card("State-of-the-Art ML", "Powered by advanced algorithms including XGBoost and Random Forest for highly accurate predictions.", "🧠")
    with c2:
        glass_card("AI Insights", "Get automated, actionable business recommendations to retain at-risk customers instantly.", "💡")
    with c3:
        glass_card("Interactive Analytics", "Explore your data with professional Plotly dashboards and understand churn drivers.", "📊")

# --- PAGE: Dashboard ---
elif selected == "Dashboard":
    st.title("Executive Dashboard")
    st.markdown("High-level project metrics and dataset statistics.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        kpi_card("Total Customers", "7,043", "Analyzed in Dataset", "👥")
    with col2:
        kpi_card("Accuracy", "85.4%", "Test Set Performance", "🎯")
    with col3:
        kpi_card("Best Model", "XGBoost", "Gradient Boosting", "⚙️")
    with col4:
        kpi_card("Model Status", "Active", "Production Ready", "✅")
        
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(plot_customer_distribution(), use_container_width=True)
    with c2:
        st.plotly_chart(plot_feature_importance(), use_container_width=True)

# --- PAGE: Predict & AI Insights ---
elif selected == "Predict":
    st.title("Customer Prediction Engine")
    st.markdown("Enter customer details below to predict churn probability and generate retention strategies.")
    
    with st.form("prediction_form"):
        st.markdown("### 👤 Customer Information")
        c1, c2, c3 = st.columns(3)
        with c1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            senior = st.selectbox("Senior Citizen", ["Yes", "No"])
        with c2:
            partner = st.selectbox("Partner", ["Yes", "No"])
            dependents = st.selectbox("Dependents", ["Yes", "No"])
        with c3:
            tenure = st.number_input("Tenure (Months)", min_value=0, max_value=120, value=12)
            
        st.markdown("### 🌐 Service Information")
        c1, c2, c3 = st.columns(3)
        with c1:
            phone = st.selectbox("Phone Service", ["Yes", "No"])
            multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
        with c2:
            internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            online_sec = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
        with c3:
            online_back = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
            device_prot = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
            
        c1, c2, c3 = st.columns(3)
        with c1:
            tech_sup = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
        with c2:
            stream_tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
        with c3:
            stream_mov = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
            
        st.markdown("### 💳 Billing & Contract")
        c1, c2, c3 = st.columns(3)
        with c1:
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
        with c2:
            payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        with c3:
            monthly_charge = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=500.0, value=70.0)
            total_charge = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=840.0)
            
        submit = st.form_submit_button("Predict Customer Risk", use_container_width=True)
        
        if submit:
            input_dict = {
                "Gender": gender, "Senior Citizen": senior, "Partner": partner,
                "Dependents": dependents, "Tenure Months": tenure, "Phone Service": phone,
                "Multiple Lines": multiple_lines, "Internet Service": internet,
                "Online Security": online_sec, "Online Backup": online_back,
                "Device Protection": device_prot, "Tech Support": tech_sup,
                "Streaming TV": stream_tv, "Streaming Movies": stream_mov,
                "Contract": contract, "Paperless Billing": paperless,
                "Payment Method": payment, "Monthly Charges": monthly_charge,
                "Total Charges": total_charge
            }
            
            with st.spinner("Analyzing customer profile via XGBoost model and generating SHAP explanations..."):
                prob, shap_df = predict_churn(input_dict)
                insights = generate_ai_insights(prob, input_dict, shap_df)
                
                st.session_state['prediction_made'] = True
                st.session_state['prediction_prob'] = prob
                st.session_state['input_data'] = input_dict
                st.session_state['insights'] = insights
                st.session_state['shap_df'] = shap_df

    # Show results outside the form if prediction is made
    if st.session_state.get('prediction_made'):
        st.markdown("---")
        
        # Two columns for Prediction and SHAP
        res_col1, res_col2 = st.columns([1, 1.5])
        
        with res_col1:
            st.markdown("### 📊 Prediction Result")
            prob = st.session_state['prediction_prob']
            risk_level = prediction_result_card(prob)
            st.session_state['risk_level'] = risk_level
            
        with res_col2:
            st.markdown("### 🧠 Explainable AI (SHAP)")
            shap_fig = plot_local_shap(st.session_state['shap_df'])
            st.plotly_chart(shap_fig, use_container_width=True)
        
        st.markdown("### 🤖 AI Insights & Recommendations")
        for insight in st.session_state['insights']:
            glass_card("Advisor", insight, "💡")

# --- PAGE: Analytics ---
elif selected == "Analytics":
    st.title("Data Analytics")
    st.markdown("Explore dataset trends and key churn drivers.")
    
    st.plotly_chart(plot_customer_distribution(), use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(plot_contract_distribution(), use_container_width=True)
    with col2:
        st.plotly_chart(plot_monthly_charges(), use_container_width=True)
        
    st.plotly_chart(plot_tenure_analysis(), use_container_width=True)

# --- PAGE: Reports ---
elif selected == "Reports":
    st.title("Reports & Downloads")
    st.markdown("Generate and download prediction reports.")
    
    if st.session_state.get('prediction_made'):
        st.success("✅ A recent prediction is available for export.")
        
        pdf_bytes = generate_prediction_pdf(
            st.session_state['input_data'],
            st.session_state['prediction_prob'],
            st.session_state['risk_level'],
            st.session_state['insights']
        )
        
        # We need to make sure the bytes are properly handled
        # fpdf.output(dest='S') returns a string (latin-1) in fpdf, but bytearray in fpdf2
        # Let's handle both
        if isinstance(pdf_bytes, str):
            pdf_bytes = pdf_bytes.encode('latin-1')
            
        st.download_button(
            label="📄 Download Prediction Report (PDF)",
            data=pdf_bytes,
            file_name="Prediction_Report.pdf",
            mime="application/pdf"
        )
        
        # CSV download
        df_download = pd.DataFrame([st.session_state['input_data']])
        df_download['Churn_Probability'] = st.session_state['prediction_prob']
        df_download['Risk_Level'] = st.session_state['risk_level']
        
        csv_bytes = df_download.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📊 Download Prediction Data (CSV)",
            data=csv_bytes,
            file_name="Prediction_Data.csv",
            mime="text/csv"
        )
    else:
        st.warning("No prediction has been made yet. Please go to the Predict page first.")

# --- PAGE: About ---
elif selected == "About":
    st.title("About the Platform")
    
    st.markdown("""
    ### Project Overview
    The **Customer Churn Prediction & Retention Intelligence Platform** is a premium AI SaaS designed to help telecommunications companies predict customer churn before it happens and formulate proactive retention strategies.
    
    ### Business Problem
    Customer churn costs the telecom industry billions of dollars annually. Acquiring a new customer is 5-25x more expensive than retaining an existing one. This platform provides actionable foresight and AI-driven recommendations to minimize churn rates.
    
    ### Architecture & Tech Stack
    - **Frontend:** Streamlit, Custom CSS (Glassmorphism), Plotly
    - **Machine Learning:** Scikit-Learn Pipeline, XGBoost Classifier, Random Forest
    - **Data Processing:** Pandas, NumPy
    - **Deployment:** Vercel / Streamlit Community Cloud
    
    ### Author Information
    - **Developer:** Principal AI Software Engineer
    - **GitHub:** [GitHub Profile](https://github.com)
    - **LinkedIn:** [LinkedIn Profile](https://linkedin.com)
    """)
