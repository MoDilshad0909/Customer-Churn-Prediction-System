import streamlit as st

def apply_theme():
    """
    Injects custom CSS to style the Streamlit app with a Dark Premium Theme, 
    glassmorphism, and smooth animations.
    """
    st.markdown("""
        <style>
            /* Base Theme and Typography */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                background-color: #070B1A !important;
                color: #FFFFFF;
            }
            
            /* Hide Streamlit Branding */
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}

            /* Main Container */
            .main .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                padding-left: 5rem;
                padding-right: 5rem;
                max-width: 1200px;
            }

            /* Headings */
            h1, h2, h3, h4, h5, h6 {
                color: #FFFFFF;
                font-weight: 600;
                letter-spacing: -0.5px;
            }

            h1 { font-size: 2.5rem; background: -webkit-linear-gradient(45deg, #A855F7, #3B82F6, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            h2 { font-size: 1.75rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem; margin-bottom: 1.5rem; }

            /* Glassmorphism Cards */
            .glass-card {
                background: rgba(255, 255, 255, 0.03);
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 20px;
                padding: 1.5rem;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                margin-bottom: 1.5rem;
            }
            .glass-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

            /* Buttons */
            .stButton > button {
                background: linear-gradient(135deg, #A855F7 0%, #3B82F6 100%);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 0.75rem 1.5rem;
                font-weight: 600;
                font-size: 1rem;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
                width: 100%;
            }
            .stButton > button:hover {
                transform: scale(1.02);
                box-shadow: 0 6px 20px rgba(168, 85, 247, 0.6);
                background: linear-gradient(135deg, #9333EA 0%, #2563EB 100%);
                color: white;
            }
            
            /* Success / Danger Badges */
            .badge {
                display: inline-block;
                padding: 0.5rem 1rem;
                border-radius: 9999px;
                font-weight: 600;
                font-size: 0.875rem;
                text-align: center;
                backdrop-filter: blur(8px);
            }
            .badge-success { background: rgba(16, 185, 129, 0.15); color: #10B981; border: 1px solid rgba(16, 185, 129, 0.3); }
            .badge-warning { background: rgba(245, 158, 11, 0.15); color: #F59E0B; border: 1px solid rgba(245, 158, 11, 0.3); }
            .badge-danger { background: rgba(239, 68, 68, 0.15); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.3); }
            .badge-info { background: rgba(59, 130, 246, 0.15); color: #3B82F6; border: 1px solid rgba(59, 130, 246, 0.3); }

            /* Inputs */
            .stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>div>input {
                background-color: rgba(255, 255, 255, 0.05) !important;
                color: white !important;
                border-radius: 10px !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
            }
            .stTextInput>div>div>input:focus, .stSelectbox>div>div>select:focus, .stNumberInput>div>div>input:focus {
                border-color: #A855F7 !important;
                box-shadow: 0 0 0 1px #A855F7 !important;
            }
            
            /* Sidebar */
            [data-testid="stSidebar"] {
                background-color: #0A0F24 !important;
                border-right: 1px solid rgba(255, 255, 255, 0.05);
            }
            
            /* Metric values */
            [data-testid="stMetricValue"] {
                font-size: 2rem !important;
                font-weight: 700 !important;
                background: -webkit-linear-gradient(45deg, #A855F7, #06B6D4);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            /* Progress Bar */
            .stProgress > div > div > div > div {
                background-image: linear-gradient(to right, #3B82F6, #A855F7, #EF4444);
            }
        </style>
    """, unsafe_allow_html=True)
