import streamlit as st
import pandas as pd
import requests

# Professional UI Configuration
st.set_page_config(page_title="Investment Analysis | Gold Venture", layout="wide")

# Theme Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background-color: #161b22; }
    div[data-testid="stExpander"] { border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# 1. LIVE DATA FEED (Zero-Cost Setup)
@st.cache_data(ttl=3600)
def get_gold_price():
    # In production, replace with a free API like Alpha Vantage or MetalpriceAPI
    # For now, we use your baseline as the dynamic default
    return 155000 

spot_price = get_gold_price()

# 2. HEADER & BRANDING
st.title("⚜️ Strategic Gold Venture Analysis")
st.markdown("### *Comparative Economic Modeling for Institutional Investors*")
st.divider()

# 3. INTERACTIVE MODELING (The "Stress Test")
with st.sidebar:
    st.header("🎛️ Scenario Controls")
    lbma_input = st.slider("LBMA Spot Price ($/Kg)", 120000, 200000, spot_price)
    monthly_vol = st.slider("Monthly Volume (Kg) - Scenario 1", 10, 50, 25)
    st.info("Adjust the sliders to see how market volatility expands the integrated margin gap.")

# 4. THE CALCULATIONS (Ironclad CFA Logic)
# Scenario 1: Venture
s1_profit_kg = lbma_input * 0.08
s1_annual = s1_profit_kg * monthly_vol * 12
s1_roi = (s1_annual / 870000) * 100

# Scenario 2: Dubai Spot
s2_profit_kg = lbma_input * 0.02
s2_annual = s2_profit_kg * 25 * 2
s2_roi = (s2_annual / 870000) * 100

# 5. THE DASHBOARD VIEW
col1, col2 = st.columns(2)

with col1:
    st.subheader("Scenario 1: Integrated Venture")
    st.metric(label="Projected Year-1 Profit", value=f"${s1_annual:,.0f}", delta=f"{s1_roi:.1f}% ROI")
    st.caption("Includes: Refinery, Lab, Logistics, and 8% ROFR Perpetual Yield.")

with col2:
    st.subheader("Scenario 2: Dubai Spot Trade")
    st.metric(label="Projected Year-1 Profit", value=f"${s2_annual:,.0f}", delta=f"{s2_roi:.1f}% ROI", delta_color="inverse")
    st.caption("Standard 3rd-party transaction at 2% discount (Bi-annual frequency).")

st.divider()

# 6. GRAPHIC REPRESENTATION
chart_data = pd.DataFrame({
    "Scenario": ["Venture (Integrated)", "Dubai (Spot)"],
    "Annual Profit ($)": [s1_annual, s2_annual]
})
st.bar_chart(chart_data, x="Scenario", y="Annual Profit ($)", color="#d4af37")

# 7. THE "SUBLIME" CONCLUSION (Dynamic Copy)
st.header("Executive Summary & Conclusion")
profit_delta = s1_annual - s2_annual

st.markdown(f"""
> **The Analysis:** At a gold price of **${lbma_input:,.0f}/Kg**, the vertically integrated venture (Scenario 1) outperforms 
> traditional spot trading by **${profit_delta:,.0f}** annually. 
>
> **The Institutional Advantage:** Scenario 2 is limited by market 'access' and third-party margins. Scenario 1 
> creates a structural advantage by capturing the full 800 basis point spread. This is not merely a trading strategy; 
> it is an infrastructure play that yields **{s1_roi/s2_roi:.1f}x** the capital efficiency of the spot market.
""")

with st.expander("View Financial Assumptions & Facts"):
    st.write("""
    - **Principal:** $870,000 USD
    - **Note Floor:** 20% 6-month yield guaranteed regardless of gold volume.
    - **ROFR:** Perpetual right to 25Kg/month at 8% below LBMA.
    - **Risk Mitigation:** All final assays and settlements occur in Tier-1 Dubai Refineries.
    """)