import pandas as pd
from fpdf import FPDF
import datetime
import io

def generate_prediction_pdf(input_data, probability, risk_level, insights):
    """
    Generates a PDF report for a specific prediction.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Fonts
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Customer Churn Prediction Report", ln=True, align="C")
    
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 10, f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.line(10, 30, 200, 30)
    
    # Prediction Result
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Prediction Result", ln=True)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 10, "Churn Probability:", ln=False)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"{probability*100:.1f}%", ln=True)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 10, "Risk Level:", ln=False)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"{risk_level}", ln=True)
    
    # AI Insights
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "AI Insights & Recommendations", ln=True)
    
    pdf.set_font("Arial", '', 11)
    for insight in insights:
        # Simple cleanup of markdown bolding
        clean_insight = insight.replace('**', '')
        pdf.multi_cell(0, 8, f"- {clean_insight}")
        
    # Input Data
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, "Customer Profile", ln=True)
    
    pdf.set_font("Arial", '', 11)
    for key, value in input_data.items():
        pdf.cell(80, 8, f"{key}:", ln=False)
        pdf.cell(0, 8, f"{value}", ln=True)
        
    # Output as byte string
    # Try using output(dest='S').encode('latin-1') for fpdf2 byte output
    return pdf.output(dest='S')
