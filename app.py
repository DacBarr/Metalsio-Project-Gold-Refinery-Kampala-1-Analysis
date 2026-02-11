import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. PAGE CONFIG & PREMIUM THEME ---
st.set_page_config(page_title="Institutional Gold Analysis", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: #FFFFFF; font-family: 'Inter', sans-serif; }
    .metric-card {
        background-color: #161B22; border: 2px solid #D4AF37;
        padding: 30px; border-radius: 15px; text-align: center;
        box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.6);
    }
    .metric-label { font-size: 1.1rem; color: #8B949E; text-transform: uppercase; letter-spacing: 1px; }
    .metric-value { font-size: 3.2rem; font-weight: 800; color: #D4AF37; margin: 10px 0; }
    .metric-roi { font-size: 1.6rem; font-weight: 600; color: #238636; }
    .main-title { font-size: 3.5rem; font-weight: 900; text-align: center; margin-bottom: 0px; }
    .sub-title { font-size: 1.4rem; text-align: center; color: #D4AF37; margin-bottom: 50px; opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown('<h1 class="main-title">⚜️ STRATEGIC GOLD VENTURE</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Net Yield Modeling & Operational Sensitivity</p>', unsafe_allow_html=True)

# --- 3. INPUTS & DYNAMIC OPEX ---
with st.sidebar:
    st.header("🎛️ Market Parameters")
    base_price = st.slider("LBMA Spot Price ($/Kg)", 130000, 190000, 155000)
    monthly_kg = st.slider("S1 Monthly Volume (Kg)", 10, 50, 25)
    
    st.header("🏢 Operational Expenses (OpEx)")
    s1_opex_monthly = st.number_input("S1 Monthly Overhead ($)", value=35000, help="Refinery, Staff, Security, Logistics")
    s2_opex_per_trade = st.number_input("S2 Cost Per Trade ($)", value=7500, help="Brokerage, Legal, Insurance")

# --- 4. CALCULATIONS (NET PROFIT FOCUS) ---
principal = 870000

# Scenario 1 Calculations
s1_gross = (base_price * 0.08) * monthly_kg * 12
s1_total_opex = s1_opex_monthly * 12
s1_net = s1_gross - s1_total_opex
s1_roi = (s1_net / principal) * 100

# Scenario 2 Calculations
s2_gross = (base_price * 0.02) * 25 * 2
s2_total_opex = s2_opex_per_trade * 2
s2_net = s2_gross - s2_total_opex
s2_roi = (s2_net / principal) * 100

# --- 5. BOTTOM-LINE METRICS ---
col1, col2 = st.columns(2)
with col1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">S1: Net Annual Profit</div><div class="metric-value">${s1_net:,.0f}</div><div class="metric-roi">{s1_roi:.1f}% NET ROI</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">S2: Net Annual Profit</div><div class="metric-value">${s2_net:,.0f}</div><div class="metric-roi">{s2_roi:.1f}% NET ROI</div></div>', unsafe_allow_html=True)

st.write("### ")

# --- 6. PROFIT WATERFALL VISUALIZATION ---
st.header("📉 Gross vs. Net Profit Breakdown")
comparison_data = pd.DataFrame({
    'Metric': ['Gross Profit', 'Gross Profit', 'OpEx (Annual)', 'OpEx (Annual)', 'Net Profit', 'Net Profit'],
    'Value': [s1_gross, s2_gross, s1_total_opex, s2_total_opex, s1_net, s2_net],
    'Scenario': ['Venture (S1)', 'Dubai (S2)', 'Venture (S1)', 'Dubai (S2)', 'Venture (S1)', 'Dubai (S2)']
})
st.bar_chart(comparison_data, x="Metric", y="Value", color="Scenario")

# --- 7. NET SENSITIVITY HEATMAP ---
st.header("📊 Net Profit Sensitivity Matrix")
st.write("Examines Net Annual Profit ($M) relative to LBMA price fluctuations and varying Discount Rates.")

prices = np.linspace(base_price * 0.8, base_price * 1.2, 5)
discounts = [0.06, 0.07, 0.08, 0.09, 0.10]
matrix = np.zeros((len(discounts), len(prices)))

for i, d in enumerate(discounts):
    for j, p in enumerate(prices):
        matrix[i, j] = ((p * d) * monthly_kg * 12) - s1_total_opex

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#0E1117')
ax.set_facecolor('#0E1117')
sns.heatmap(matrix / 1000000, annot=True, fmt=".2f", cmap="YlOrBr", 
            xticklabels=[f"${x/1000:,.0f}k" for x in prices], 
            yticklabels=[f"{x*100:.0f}%" for x in discounts], ax=ax)
plt.title("Scenario 1: Net Profit Sensitivity ($M)", color='#D4AF37', fontsize=14)
ax.tick_params(colors='white')
st.pyplot(fig)
