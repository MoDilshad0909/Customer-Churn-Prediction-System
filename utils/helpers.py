import pandas as pd
from fpdf import FPDF
import datetime
import io

def clean_text_for_pdf(text):
    """
    Cleans text by replacing emojis with their plain text equivalents 
    and removing unsupported unicode characters for PDF rendering.
    """
    if not isinstance(text, str):
        text = str(text)
        
    replacements = {
        '✅': 'Success',
        '🟢': 'Low Risk',
        '🔴': 'High Risk',
        '🟡': 'Moderate Risk',
        '📊': 'Analytics',
        '📈': 'Trend',
        '💡': 'Recommendation:',
        '⭐': 'Star',
        '🚀': 'Launch',
        '🎯': 'Target',
        '✔️': 'Check',
        '❌': 'Cross',
        '🚨': 'Warning',
        '⚠️': 'Alert',
        '🔍': 'Analysis:',
        '🧠': 'AI:'
    }
    
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
        
    # Replace any other unicode character not supported by latin-1
    return text.encode('latin-1', 'replace').decode('latin-1')

def generate_prediction_pdf(input_data, probability, risk_level, insights):
    """
    Generates a PDF report for a specific prediction.
    """
    pdf = FPDF()
    pdf.add_page()
    
    # Fonts
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, clean_text_for_pdf("Customer Churn Prediction Report"), ln=True, align="C")
    
    pdf.set_font("Arial", '', 10)
    pdf.cell(0, 10, clean_text_for_pdf(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"), ln=True, align="C")
    pdf.line(10, 30, 200, 30)
    
    # Prediction Result
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, clean_text_for_pdf("Prediction Result"), ln=True)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 10, clean_text_for_pdf("Churn Probability:"), ln=False)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, clean_text_for_pdf(f"{probability*100:.1f}%"), ln=True)
    
    pdf.set_font("Arial", '', 12)
    pdf.cell(50, 10, clean_text_for_pdf("Risk Level:"), ln=False)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, clean_text_for_pdf(f"{risk_level}"), ln=True)
    
    # AI Insights
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, clean_text_for_pdf("AI Insights & Recommendations"), ln=True)
    
    pdf.set_font("Arial", '', 11)
    for insight in insights:
        # Simple cleanup of markdown bolding
        clean_insight = insight.replace('**', '')
        pdf.multi_cell(0, 8, clean_text_for_pdf(f"- {clean_insight}"))
        
    # Input Data
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, clean_text_for_pdf("Customer Profile"), ln=True)
    
    pdf.set_font("Arial", '', 11)
    for key, value in input_data.items():
        pdf.cell(80, 8, clean_text_for_pdf(f"{key}:"), ln=False)
        pdf.cell(0, 8, clean_text_for_pdf(f"{value}"), ln=True)
        
    # Output as byte string
    # Try using output(dest='S').encode('latin-1') for fpdf2 byte output
    return pdf.output(dest='S')
