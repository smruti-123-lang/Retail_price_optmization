````markdown
# 🏷️ Price Elasticity Engine

> Predicts how sensitive product demand is to price changes — the same problem Amazon and Flipkart's pricing teams solve at scale. Built on real Brazilian e-commerce data with competitor pricing signals, seasonal patterns, and product quality metrics.

<br>

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.18-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)

<br>

## 🚀 Live Demo

**[👉 Click here to try the app](#)** ← *https://dfdppef5rrfrtyrchcw5oa.streamlit.app/*

<br>

---

## 💡 The Problem

Every e-commerce seller faces this question daily:

> *"If I increase my price by ₹100, how many customers will I lose? Is it still worth it?"*

Most sellers guess. This project answers it with data and ML.

**Real scenario this model solves:**
````
You sell a gaming console at ₹12,999
Competitor is selling at ₹11,499
Your rating is 4.2, theirs is 3.8
It's a holiday weekend

→ Should you lower your price?
→ By how much?
→ What's the demand impact?

Your model answers all three.
````

---

## 📊 Dataset

Real Brazilian e-commerce retail pricing data.

| Property | Value |
|----------|-------|
| Rows | 676 |
| Features | 30 |
| Time Period | 2017 – 2018 |
| Missing Values | 0 (perfectly clean) |
| Product Categories | 9 |
| Price Range | ₹19.9 – ₹364.0 |
| Demand Range | 1 – 122 units/month |

**9 Product Categories:**
`bed_bath_table` · `garden_tools` · `consoles_games` · `health_beauty` · `cool_stuff` · `perfumery` · `computers_accessories` · `watches_gifts` · `furniture_decor`

---

## 🔍 Key EDA Findings

**Finding 1 — Target variable was heavily skewed**
````
qty skewness before log transform : 2.67  ← heavily skewed
qty skewness after log transform  : -0.01 ← near perfect normality
````
Applied log1p transform to satisfy Linear Regression's normality assumption.

**Finding 2 — Different categories have different demand patterns**
````
bed_bath_table  → high volume (50+ units/month)
consoles_games  → low volume, niche category
health_beauty   → moderate, consistent demand
garden_tools    → dominant category in dataset
````

**Finding 3 — Price alone doesn't explain demand**
````
At price = ₹100:
Some products sell 2-3 units
Some products sell 50+ units

→ Competitor price, rating, shipping,
  category all matter equally
````

---

## ⚙️ Feature Engineering

| Feature Created | Formula | Insight |
|----------------|---------|---------|
| `price_vs_market` | `unit_price / avg(comp_1,2,3)` | Relative price position |
| `price_change` | `unit_price - lag_price` | Month-on-month movement |
| `avg_comp_score` | `mean(ps1, ps2, ps3)` | Competitor quality signal |
| `freight_advantage` | `avg_comp_freight - freight_price` | Shipping competitiveness |
| `is_free_shipping` | `1 if freight == 0` | Binary boost signal |

**Key discovery from feature engineering:**
````
238 out of 676 products (35%) are priced BELOW competitors
65% of sellers price ABOVE market
→ Rating and product quality justify the premium
→ rating_advantage becomes a critical feature
````

---

## 🤖 Models & Results

Started with Linear Regression as an interpretable baseline,
then applied regularization techniques.

| Model | R² Score | RMSE | Notes |
|-------|---------|------|-------|
| Linear Regression | 0.2626 | 0.7806 | Baseline |
| Ridge (L2) | 0.2637 | 0.7800 | Handles multicollinearity |
| **Lasso (L1)** | **0.2681** | **0.7776** | **Selected ✅** |

**Why R² of 0.27 is expected and acceptable:**
````
Price vs demand is inherently non-linear
Linear models hit a natural ceiling here
All three models scoring similarly confirms
underfitting — not overfitting
→ XGBoost is the planned next step
````

**Multicollinearity fix improved LR from 0.2186 → 0.2626:**
````
8 correlated features removed:
lag_price, avg_comp_price, price_gap_comp1,
rating_advantage, avg_comp_freight,
log_unit_price, log_freight, log_comp1
````

---

## 🖥️ App Features

````
├── 4 Live Metric Cards
│   ├── Predicted units sold
│   ├── Your price vs market average
│   ├── Shipping competitiveness
│   └── Rating vs competitors
│
├── Interactive Price vs Demand Curve
│   └── See how demand shifts as you move price
│
├── What-If Price Analysis
│   ├── Impact of 10% price drop
│   ├── Current position
│   └── Impact of 10% price rise
│
├── Model Comparison Table
│   └── LR vs Ridge vs Lasso metrics
│
└── Business Insight
    └── Automated pricing recommendation
````

---

## 🏗️ Project Structure

````
price-elasticity-engine/
│
├── data/
│   └── retail_price.csv          ← Real Brazilian e-commerce data
│
├── notebooks/
│   ├── 01_EDA.ipynb              ← Exploratory analysis & findings
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb         ← Model training & evaluation
│
├── models/
│   ├── lasso_model.pkl           ← Saved Lasso model
│   ├── scaler.pkl                ← Saved StandardScaler
│   └── feature_names.pkl         ← Saved feature order
│
├── app.py                        ← Streamlit dashboard
├── requirements.txt
└── README.md
````

---

## ▶️ Run Locally

```bash
# Clone the repo
git clone https://github.com/yourusername/price-elasticity-engine
cd price-elasticity-engine

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📦 Requirements

````
pandas
numpy
scikit-learn
streamlit
plotly
joblib
````

---

## 🗺️ Roadmap

- [x] EDA & data cleaning
- [x] Feature engineering
- [x] Linear Regression baseline
- [x] Ridge & Lasso regularization
- [x] Streamlit dashboard
- [x] Deployment
- [ ] XGBoost model (next step)
- [ ] SHAP explainability
- [ ] Category-wise elasticity breakdown
- [ ] Real-time price scraping

---

## 🎯 Interview Narrative

> *"I built a price elasticity engine that answers the question every e-commerce seller faces daily — if I change my price, how will my sales change? Using real retail data with competitor pricing signals, I built a model that captures not just your price but how it compares to 3 competitors, your rating advantage, shipping cost competitiveness, and seasonal demand patterns. The target variable had a skewness of 2.67 which I corrected to -0.01 using log transform. After fixing multicollinearity across 8 correlated features, I compared Linear Regression, Ridge and Lasso — selecting Lasso for its built-in feature selection via L1 regularization. The similar performance across all three models confirmed underfitting rather than overfitting, motivating XGBoost as the next step."*

---

## 👤 Author

**Your Name**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com)

---

⭐ **Star this repo if it helped you!**
````
