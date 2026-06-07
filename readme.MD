# 🏷️ Price Elasticity Engine

> Predicts how sensitive product demand is to price changes — the same problem Amazon and Flipkart's pricing teams solve at scale. Built on real Brazilian e-commerce data with competitor pricing signals, seasonal patterns, and product quality metrics.

<br>

[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square\&logo=python\&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3-F7931E?style=flat-square\&logo=scikit-learn\&logoColor=white)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B?style=flat-square\&logo=streamlit\&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.18-3F4F75?style=flat-square\&logo=plotly\&logoColor=white)](https://plotly.com)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?style=flat-square\&logo=pandas\&logoColor=white)](https://pandas.pydata.org)

---

## 🚀 Live Demo

**👉 [Try the Streamlit App](https://dfdppef5rrfrtyrchcw5oa.streamlit.app/)**

---

## 💡 The Problem

Every e-commerce seller faces this question daily:

> "If I increase my price by ₹100, how many customers will I lose? Is it still worth it?"

Most sellers guess. This project answers it with data and machine learning.

### Example Scenario

You sell a gaming console at ₹12,999

Competitor price: ₹11,499

Your rating: 4.2

Competitor rating: 3.8

Holiday weekend active

Questions:

* Should you lower your price?
* By how much?
* What will happen to demand?

This model provides data-driven answers.

---

## 📊 Dataset

Real Brazilian e-commerce retail pricing data.

| Property       | Value             |
| -------------- | ----------------- |
| Rows           | 676               |
| Features       | 30                |
| Time Period    | 2017–2018         |
| Missing Values | 0                 |
| Categories     | 9                 |
| Price Range    | ₹19.9 – ₹364      |
| Demand Range   | 1–122 units/month |

### Categories

* bed_bath_table
* garden_tools
* consoles_games
* health_beauty
* cool_stuff
* perfumery
* computers_accessories
* watches_gifts
* furniture_decor

---

## 🔍 Exploratory Data Analysis

### Target Distribution

qty skewness before transform = 2.67

qty skewness after log1p transform = -0.01

Applied log transformation to satisfy linear model assumptions.

### Category Insights

* bed_bath_table shows high volume demand
* consoles_games is niche and low volume
* health_beauty exhibits stable demand
* garden_tools dominates the dataset

### Price Alone Is Not Enough

Products at the same price often have drastically different demand.

Other important factors:

* Competitor prices
* Ratings
* Shipping costs
* Product category
* Seasonality

---

## ⚙️ Feature Engineering

| Feature           | Formula                               |
| ----------------- | ------------------------------------- |
| price_vs_market   | unit_price / avg(comp1, comp2, comp3) |
| price_change      | unit_price - lag_price                |
| avg_comp_score    | mean(ps1, ps2, ps3)                   |
| freight_advantage | avg_comp_freight - freight_price      |
| is_free_shipping  | freight_price == 0                    |

### Key Discovery

* 35% products priced below competitors
* 65% priced above competitors

Premium pricing is often justified by:

* Better ratings
* Better product quality
* Better shipping experience

---

## 🤖 Model Performance

| Model             | R²     | RMSE   |
| ----------------- | ------ | ------ |
| Linear Regression | 0.2626 | 0.7806 |
| Ridge Regression  | 0.2637 | 0.7800 |
| Lasso Regression  | 0.2681 | 0.7776 |

### Selected Model

✅ Lasso Regression

Reasons:

* Best performance
* Automatic feature selection
* Simpler deployment

### Multicollinearity Reduction

Performance improved:

0.2186 → 0.2626

Removed:

* lag_price
* avg_comp_price
* price_gap_comp1
* rating_advantage
* avg_comp_freight
* log_unit_price
* log_freight
* log_comp1

---

## 🖥️ Dashboard Features

### Live Metrics

* Predicted Units Sold
* Price vs Market
* Shipping Advantage
* Rating Advantage

### Interactive Demand Curve

Visualize demand sensitivity as price changes.

### What-If Analysis

Compare:

* 10% price decrease
* Current price
* 10% price increase

### Model Comparison

Performance comparison between:

* Linear Regression
* Ridge
* Lasso

### Automated Business Recommendation

Provides pricing suggestions based on predicted demand.

---

## 🏗️ Project Structure

```text
price-elasticity-engine/

├── data/
│   └── retail_price.csv

├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb

├── models/
│   ├── lasso_model.pkl
│   ├── scaler.pkl
│   └── feature_names.pkl

├── app.py
├── requirements.txt
└── README.md
```

## ▶️ Run Locally

```bash
git clone https://github.com/yourusername/price-elasticity-engine

cd price-elasticity-engine

pip install -r requirements.txt

streamlit run app.py
```

## 📦 Requirements

```txt
pandas
numpy
scikit-learn
streamlit
plotly
joblib
```

## 🗺️ Future Improvements

* [x] EDA
* [x] Feature Engineering
* [x] Linear Regression
* [x] Ridge Regression
* [x] Lasso Regression
* [x] Streamlit Deployment
* [ ] XGBoost
* [ ] SHAP Explainability
* [ ] Category Elasticity Analysis
* [ ] Real-Time Price Scraping

## 🎯 Interview Pitch

"I built a Price Elasticity Engine that predicts how demand changes when product prices change. Using competitor pricing, ratings, shipping costs, and seasonal patterns, I engineered market-relative features and trained Linear Regression, Ridge, and Lasso models. After correcting target skewness and removing multicollinear features, Lasso achieved the best performance and was selected for deployment. The project demonstrates pricing analytics, feature engineering, machine learning, and business decision support."

## 👤 Author

**Smruti Misra**

GitHub: https://github.com/smruti-123-lang

Portfolio: https://vercel.com/smruti-123-langs-projects

LinkedIn: Add your LinkedIn profile here

⭐ If you found this project useful, consider starring the repository.
