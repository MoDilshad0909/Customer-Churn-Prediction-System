import streamlit as st

def badge(text, type='info'):
    """
    Renders a styled badge.
    Types: success, warning, danger, info
    """
    return f'<span class="badge badge-{type}">{text}</span>'

def glass_card(title, content, icon="📊"):
    """
    Renders content inside a glassmorphism card.
    """
    html = f"""
    <div class="glass-card">
        <h4 style="margin-top:0;">{icon} {title}</h4>
        <p style="color: #cbd5e1; margin-bottom: 0;">{content}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def kpi_card(title, value, subtitle="", icon="📈"):
    """
    Renders an executive KPI card.
    """
    html = f"""
    <div class="glass-card" style="text-align: center;">
        <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
        <div style="font-size: 0.9rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">{title}</div>
        <div style="font-size: 2.2rem; font-weight: 700; background: -webkit-linear-gradient(45deg, #A855F7, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{value}</div>
        <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.5rem;">{subtitle}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def prediction_result_card(probability, threshold=0.5):
    """
    Renders the prediction result using badges and animations.
    """
    if probability > threshold:
        risk = "High"
        b_type = "danger"
        title = "Customer Will Churn 🚨"
        msg = "Immediate retention action is required."
        color = "#EF4444"
    elif probability > 0.3:
        risk = "Medium"
        b_type = "warning"
        title = "Customer is at Risk ⚠️"
        msg = "Monitor closely and consider proactive engagement."
        color = "#F59E0B"
    else:
        risk = "Low"
        b_type = "success"
        title = "Customer Will Stay ✅"
        msg = "Customer is highly likely to remain subscribed."
        color = "#10B981"
        
    html = f"""
    <div class="glass-card" style="border-left: 4px solid {color}; text-align: center; padding: 2rem;">
        <h2 style="color: {color}; font-size: 2rem;">{title}</h2>
        <div style="margin: 1.5rem 0;">
            <span style="font-size: 1.2rem; color: #94a3b8;">Risk Level: </span>
            {badge(risk, b_type)}
        </div>
        <div style="font-size: 1.2rem; margin-bottom: 1rem;">
            Probability of Churn: <span style="font-weight: bold; font-size: 1.5rem;">{probability*100:.1f}%</span>
        </div>
        <p style="color: #cbd5e1; font-style: italic;">{msg}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    return risk
