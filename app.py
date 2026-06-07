import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

st.set_page_config(
    page_title="Price Elasticity Engine",
    page_icon="🏷️",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

    * { font-family: 'IBM Plex Sans', sans-serif !important; }

    /* BACKGROUND */
    .stApp {
        background-color: #0a0e17;
        background-image:
            radial-gradient(ellipse at 20% 50%, rgba(0, 255, 136, 0.04) 0%, transparent 60%),
            radial-gradient(ellipse at 80% 20%, rgba(0, 122, 255, 0.05) 0%, transparent 60%);
    }

    .block-container { padding-top: 1.5rem; max-width: 1400px; }

    /* ALL TEXT — bright by default */
    p, div, span, label {
        color: #e2e8f0 !important;
    }

    .stMarkdown p {
        color: #e2e8f0 !important;
        font-size: 0.95rem !important;
    }

    /* TITLE */
    h1 {
        font-family: 'IBM Plex Mono', monospace !important;
        color: #ffffff !important;
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px;
        border-bottom: 1px solid #1e2d40;
        padding-bottom: 0.8rem;
    }

    /* SUBHEADERS */
    h2, h3 {
        font-family: 'IBM Plex Mono', monospace !important;
        color: #e2e8f0 !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 1rem !important;
    }

    /* METRIC CARDS */
    [data-testid="stMetric"] {
        background: #0d1117 !important;
        border: 1px solid #2d3748 !important;
        border-top: 2px solid #00ff88 !important;
        border-radius: 6px !important;
        padding: 18px 20px !important;
        transition: all 0.2s ease;
    }

    [data-testid="stMetric"]:hover {
        border-color: #00ff88 !important;
        box-shadow: 0 0 24px rgba(0, 255, 136, 0.12);
        transform: translateY(-2px);
    }

    [data-testid="stMetricLabel"] p {
        color: #a0aec0 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.72rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 1.6rem !important;
        font-weight: 700 !important;
    }

    [data-testid="stMetricDelta"] svg { display: none; }
    [data-testid="stMetricDelta"] > div {
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.82rem !important;
        color: #a0aec0 !important;
    }

    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background: #080c12 !important;
        border-right: 1px solid #1e2d40 !important;
    }

    [data-testid="stSidebar"] * {
        color: #cbd5e0 !important;
    }

    [data-testid="stSidebar"] h2 {
        color: #00ff88 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.68rem !important;
        font-weight: 600 !important;
        letter-spacing: 3px;
        border-bottom: 1px solid #1e2d40;
        padding-bottom: 6px;
        margin-top: 1.2rem !important;
    }

    [data-testid="stSidebar"] label {
        color: #cbd5e0 !important;
        font-size: 0.82rem !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-weight: 500 !important;
    }

    [data-testid="stSidebar"] p {
        color: #cbd5e0 !important;
        font-family: 'IBM Plex Mono', monospace !important;
    }

    /* SLIDER */
    [data-testid="stSlider"] > div > div > div > div { background: #00ff88 !important; }
    [data-testid="stSlider"] > div > div > div { background: #2d3748 !important; }
    [data-testid="stSlider"] p {
        color: #00ff88 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.82rem !important;
        font-weight: 600 !important;
    }

    /* SELECTBOX */
    [data-testid="stSelectbox"] > div > div {
        background: #0d1117 !important;
        border: 1px solid #2d3748 !important;
        border-radius: 4px !important;
        color: #ffffff !important;
        font-family: 'IBM Plex Mono', monospace !important;
    }

    /* DIVIDER */
    hr { border-color: #1e2d40 !important; margin: 1.4rem 0 !important; }

    /* DATAFRAME */
    [data-testid="stDataFrame"] {
        border: 1px solid #2d3748 !important;
        border-radius: 6px !important;
        overflow: hidden;
    }

    /* ALERT BOXES */
    [data-testid="stAlert"] {
        border-radius: 6px !important;
        border-left-width: 3px !important;
        background: #0d1117 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.88rem !important;
        color: #e2e8f0 !important;
    }

    [data-testid="stAlert"] p {
        color: #e2e8f0 !important;
        font-size: 0.88rem !important;
    }

    /* CAPTION */
    [data-testid="stCaptionContainer"] p {
        color: #4a5568 !important;
        font-family: 'IBM Plex Mono', monospace !important;
        font-size: 0.72rem !important;
        text-align: center;
        letter-spacing: 1px;
    }

    /* PLOTLY */
    .js-plotly-plot {
        border: 1px solid #2d3748 !important;
        border-radius: 6px !important;
    }

    /* SCROLLBAR */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: #080c12; }
    ::-webkit-scrollbar-thumb { background: #2d3748; border-radius: 2px; }
    ::-webkit-scrollbar-thumb:hover { background: #00ff88; }
    </style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────
@st.cache_resource
def load_model():
    model    = joblib.load('models/lasso_model.pkl')
    scaler   = joblib.load('models/scaler.pkl')
    features = joblib.load('models/feature_names.pkl')
    return model, scaler, features

model, scaler, feature_names = load_model()

# ─────────────────────────────────────
# HEADER
# ─────────────────────────────────────
st.markdown("""
    <h1>🏷️ Price Elasticity Engine</h1>
    <p style="color: #a0aec0 !important; font-size: 1rem; margin-bottom: 1rem;">
        Predict how your pricing decisions affect product demand —
        the same problem Amazon & Flipkart solve at scale.
    </p>
""", unsafe_allow_html=True)
st.divider()

# ─────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────
st.sidebar.header("⚙️ Product Parameters")

st.sidebar.subheader("💰 Pricing")
unit_price    = st.sidebar.slider("Your Price (₹)",         19.0, 364.0, 100.0, step=1.0)
comp_1        = st.sidebar.slider("Competitor 1 Price (₹)", 19.0, 364.0,  95.0, step=1.0)
comp_2        = st.sidebar.slider("Competitor 2 Price (₹)", 19.0, 364.0, 105.0, step=1.0)
comp_3        = st.sidebar.slider("Competitor 3 Price (₹)", 19.0, 364.0, 110.0, step=1.0)
freight_price = st.sidebar.slider("Your Shipping Cost (₹)", 0.0,  80.0,  20.0,  step=0.5)

st.sidebar.subheader("⭐ Ratings")
product_score = st.sidebar.slider("Your Rating",         3.3, 4.5, 4.0, step=0.1)
ps1           = st.sidebar.slider("Competitor 1 Rating", 3.3, 4.5, 3.9, step=0.1)
ps2           = st.sidebar.slider("Competitor 2 Rating", 3.3, 4.5, 4.0, step=0.1)
ps3           = st.sidebar.slider("Competitor 3 Rating", 3.3, 4.5, 4.1, step=0.1)

st.sidebar.subheader("🚚 Competitor Shipping")
fp1 = st.sidebar.slider("Competitor 1 Shipping (₹)", 0.0, 80.0, 18.0, step=0.5)
fp2 = st.sidebar.slider("Competitor 2 Shipping (₹)", 0.0, 80.0, 19.0, step=0.5)
fp3 = st.sidebar.slider("Competitor 3 Shipping (₹)", 0.0, 80.0, 17.0, step=0.5)

st.sidebar.subheader("📦 Product Info")
category = st.sidebar.selectbox("Category", [
    'bed_bath_table', 'garden_tools', 'consoles_games',
    'health_beauty', 'cool_stuff', 'perfumery',
    'computers_accessories', 'watches_gifts', 'furniture_decor'
])
product_photos_qty         = st.sidebar.slider("Number of Photos",   1,    20,   3)
product_weight_g           = st.sidebar.slider("Weight (grams)",      100, 5000, 500)
product_name_lenght        = st.sidebar.slider("Product Name Length", 10,  100,  50)
product_description_lenght = st.sidebar.slider("Description Length",  100, 3000, 800)

st.sidebar.subheader("📅 Timing")
holiday = st.sidebar.selectbox("Holiday Period?", [0, 1], format_func=lambda x: "Yes 🎉" if x == 1 else "No")
weekend = st.sidebar.slider("Weekend Days This Month", 0, 10, 8)
weekday = st.sidebar.slider("Weekday Days This Month", 0, 25, 22)
month   = st.sidebar.slider("Month", 1, 12, 6)
year    = st.sidebar.selectbox("Year", [2017, 2018])

# ─────────────────────────────────────
# FEATURE ENGINEERING
# ─────────────────────────────────────
def build_features(unit_price, comp_1, comp_2, comp_3,
                   product_score, ps1, ps2, ps3,
                   freight_price, fp1, fp2, fp3,
                   holiday, weekend, weekday, month, year,
                   category, product_photos_qty, product_weight_g,
                   product_name_lenght, product_description_lenght):

    avg_comp_price    = (comp_1 + comp_2 + comp_3) / 3
    price_vs_market   = unit_price / avg_comp_price if avg_comp_price > 0 else 1
    price_change      = 0
    is_free_shipping  = 1 if freight_price == 0 else 0
    avg_comp_score    = (ps1 + ps2 + ps3) / 3
    avg_comp_freight  = (fp1 + fp2 + fp3) / 3
    freight_advantage = avg_comp_freight - freight_price
    volume            = product_weight_g * 1.0
    s                 = 0

    data = {
        'freight_price':               freight_price,
        'unit_price':                  unit_price,
        'product_name_lenght':         product_name_lenght,
        'product_description_lenght':  product_description_lenght,
        'product_photos_qty':          product_photos_qty,
        'product_weight_g':            product_weight_g,
        'product_score':               product_score,
        'weekday':                     weekday,
        'weekend':                     weekend,
        'holiday':                     holiday,
        'month':                       month,
        'year':                        year,
        's':                           s,
        'volume':                      volume,
        'comp_1':                      comp_1,
        'ps1':                         ps1,
        'fp1':                         fp1,
        'comp_2':                      comp_2,
        'ps2':                         ps2,
        'fp2':                         fp2,
        'comp_3':                      comp_3,
        'ps3':                         ps3,
        'fp3':                         fp3,
        'price_vs_market':             price_vs_market,
        'price_change':                price_change,
        'avg_comp_score':              avg_comp_score,
        'freight_advantage':           freight_advantage,
        'is_free_shipping':            is_free_shipping,
    }

    all_categories = [
        'computers_accessories', 'consoles_games', 'cool_stuff',
        'furniture_decor', 'garden_tools', 'health_beauty',
        'perfumery', 'watches_gifts'
    ]
    for cat in all_categories:
        data[f'product_category_name_{cat}'] = 1 if category == cat else 0

    df_input = pd.DataFrame([data])
    df_input = df_input.reindex(columns=feature_names, fill_value=0)
    return df_input

# ─────────────────────────────────────
# PREDICT
# ─────────────────────────────────────
def predict_demand(price):
    df_in    = build_features(
        price, comp_1, comp_2, comp_3,
        product_score, ps1, ps2, ps3,
        freight_price, fp1, fp2, fp3,
        holiday, weekend, weekday, month, year,
        category, product_photos_qty, product_weight_g,
        product_name_lenght, product_description_lenght
    )
    scaled   = scaler.transform(df_in)
    log_pred = model.predict(scaled)[0]
    return max(int(np.expm1(log_pred)), 0)

predicted_qty    = predict_demand(unit_price)
avg_comp         = (comp_1 + comp_2 + comp_3) / 3
avg_comp_freight = (fp1 + fp2 + fp3) / 3
lower_10         = predict_demand(unit_price * 0.90)
raise_10         = predict_demand(unit_price * 1.10)

# ─────────────────────────────────────
# SECTION 3 — METRICS
# ─────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📦 Predicted Units Sold", f"{predicted_qty} units")

with col2:
    diff  = round(unit_price - avg_comp, 2)
    label = "Cheaper ✅" if diff < 0 else "More Expensive ⚠️"
    st.metric("💰 vs Market Average", label, delta=f"₹{diff}")

with col3:
    ship_diff  = round(freight_price - avg_comp_freight, 2)
    ship_label = "Cheaper Shipping ✅" if ship_diff < 0 else "Pricier Shipping ⚠️"
    st.metric("🚚 Shipping vs Competitors", ship_label, delta=f"₹{ship_diff}")

with col4:
    rating_diff  = round(product_score - (ps1 + ps2 + ps3) / 3, 2)
    rating_label = "Better Rated ✅" if rating_diff > 0 else "Lower Rated ⚠️"
    st.metric("⭐ Rating vs Competitors", rating_label, delta=f"{rating_diff}")

st.divider()

# ─────────────────────────────────────
# SECTION 4 — CHART
# ─────────────────────────────────────
st.markdown("""
    <p style="font-family:'IBM Plex Mono',monospace;
              color:#e2e8f0 !important;
              font-size:0.85rem;
              text-transform:uppercase;
              letter-spacing:3px;
              font-weight:600;">
        📈 Price vs Predicted Demand Curve
    </p>
""", unsafe_allow_html=True)

prices  = list(range(20, 365, 5))
demands = [predict_demand(p) for p in prices]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=prices, y=demands,
    mode='lines',
    fill='tozeroy',
    fillcolor='rgba(0, 255, 136, 0.06)',
    line=dict(color='#00ff88', width=2.5),
    name='Predicted Demand'
))

fig.add_vline(
    x=unit_price,
    line_dash="dash",
    line_color="#007aff",
    annotation_text=f"Your Price ₹{unit_price}",
    annotation_font_color="#7eb8ff",
    annotation_font_size=12,
    annotation_position="top right"
)

fig.add_scatter(
    x=[unit_price], y=[predicted_qty],
    mode='markers',
    marker=dict(color='#007aff', size=10, line=dict(color='#ffffff', width=1)),
    name='Current Position'
)

fig.update_layout(
    xaxis_title="PRICE (₹)",
    yaxis_title="PREDICTED UNITS SOLD",
    hovermode='x unified',
    height=420,
    plot_bgcolor='#080c12',
    paper_bgcolor='#0d1117',
    font=dict(family='IBM Plex Mono', color='#a0aec0', size=12),
    xaxis=dict(
        showgrid=True, gridcolor='#1e2d40',
        color='#cbd5e0', linecolor='#2d3748',
        tickfont=dict(color='#cbd5e0', size=11),
        title_font=dict(color='#e2e8f0', size=11)
    ),
    yaxis=dict(
        showgrid=True, gridcolor='#1e2d40',
        color='#cbd5e0', linecolor='#2d3748',
        tickfont=dict(color='#cbd5e0', size=11),
        title_font=dict(color='#e2e8f0', size=11)
    ),
    legend=dict(
        font=dict(color='#cbd5e0', size=11),
        bgcolor='rgba(0,0,0,0)',
        bordercolor='#2d3748'
    ),
    hoverlabel=dict(
        bgcolor='#0d1117',
        bordercolor='#00ff88',
        font=dict(family='IBM Plex Mono', color='#00ff88', size=12)
    ),
    margin=dict(l=60, r=30, t=30, b=60)
)

st.plotly_chart(fig, use_container_width=True)
st.divider()

# ─────────────────────────────────────
# SECTION 5 — WHAT IF
# ─────────────────────────────────────
st.markdown("""
    <p style="font-family:'IBM Plex Mono',monospace;
              color:#e2e8f0 !important;
              font-size:0.85rem;
              text-transform:uppercase;
              letter-spacing:3px;
              font-weight:600;">
        🔍 What-If Price Analysis
    </p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        f"Price drops 10% → ₹{round(unit_price*0.90, 2)}",
        f"{lower_10} units",
        delta=f"+{lower_10 - predicted_qty} units"
    )
with col2:
    st.metric(
        f"Current → ₹{unit_price}",
        f"{predicted_qty} units",
        delta="baseline"
    )
with col3:
    st.metric(
        f"Price rises 10% → ₹{round(unit_price*1.10, 2)}",
        f"{raise_10} units",
        delta=f"{raise_10 - predicted_qty} units"
    )

st.divider()

# ─────────────────────────────────────
# SECTION 6 — MODEL COMPARISON
# ─────────────────────────────────────
st.markdown("""
    <p style="font-family:'IBM Plex Mono',monospace;
              color:#e2e8f0 !important;
              font-size:0.85rem;
              text-transform:uppercase;
              letter-spacing:3px;
              font-weight:600;">
        🤖 Model Performance Comparison
    </p>
""", unsafe_allow_html=True)

model_df = pd.DataFrame({
    'Model':    ['Linear Regression', 'Ridge', 'Lasso (Selected)'],
    'R² Score': [0.2626,              0.2637,  0.2681],
    'RMSE':     [0.7806,              0.7800,  0.7776],
    'Selected': ['❌',               '❌',    '✅']
})
st.dataframe(model_df, use_container_width=True, hide_index=True)
st.caption("R² of 0.27 on log-transformed demand. Lasso selected for best generalization. XGBoost next step.")

st.divider()

# ─────────────────────────────────────
# SECTION 7 — BUSINESS INSIGHT
# ─────────────────────────────────────
st.markdown("""
    <p style="font-family:'IBM Plex Mono',monospace;
              color:#e2e8f0 !important;
              font-size:0.85rem;
              text-transform:uppercase;
              letter-spacing:3px;
              font-weight:600;">
        💡 Business Insight
    </p>
""", unsafe_allow_html=True)

if unit_price > avg_comp * 1.10:
    st.error(f"""
    ⚠️ Your price ₹{unit_price} is more than 10% above market average ₹{round(avg_comp, 2)}.
    Dropping price by 10% to ₹{round(unit_price*0.9, 2)} could increase demand
    from {predicted_qty} → {lower_10} units (+{lower_10 - predicted_qty} units).
    """)
elif unit_price < avg_comp * 0.90:
    st.success(f"""
    ✅ Your price ₹{unit_price} is well below market average ₹{round(avg_comp, 2)}.
    You may have room to raise price to ₹{round(unit_price*1.1, 2)}
    with minimal demand loss ({predicted_qty} → {raise_10} units).
    """)
else:
    st.info(f"""
    ℹ️ Your price ₹{unit_price} is competitive vs market average ₹{round(avg_comp, 2)}.
    Current predicted demand: {predicted_qty} units. Pricing looks optimal.
    """)

st.divider()
st.caption("Built with Scikit-learn · Streamlit · Plotly | Real Brazilian E-commerce Data (676 products, 9 categories)")
