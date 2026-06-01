# Nigerian House Price Predictor

A machine learning web application that predicts residential property prices in **Lagos** and **Abuja**, Nigeria. Built with scikit-learn and deployed via Streamlit.

**[Live App → Nigerian House Price Predictor](https://analysis-on-nigerian-real-estate-9nyazsbj9dfzzzrqrg5vm8.streamlit.app/)**

---

## Project Overview

Nigerian real estate pricing differs sharply by location, property type, and size, making it difficult for buyers, investors, and developers to gauge fair market value. This project addresses that gap by training a machine learning model on 24,000 property listings scraped from Nigerian real estate platforms, enabling instant price estimates from a simple web interface.

---

## Dataset

| Detail | Value |
|---|---|
| **Source** | [Kaggle; Nigerian real estate listings] (https://www.kaggle.com/datasets/michaelanietie/nigerian-house-price-dataset?resource=download) |
| **Raw records** | 24,326 |
| **After cleaning** | 13,631 |
| **Scope** | Lagos & Abuja only |
| **Target variable** | Property price (in Naira) |

**Key cleaning steps:**
- Removed 10,438 duplicate entries (42.9% of raw data caused by repeated scraping)
- Applied quantile filter (1st–99th percentile) to remove extreme price outliers
- Dropped `town` due to high cardinality (189 unique values); used `state` as geographic proxy
- Dropped `toilets` due to multicollinearity with `bathrooms` (r = 0.79)
- Dropped `parking_space` due to low correlation with price (r = 0.05)

---

## Feature Engineering

Five interaction features were engineered from the raw room count columns:

| Feature | Description |
|---|---|
| `total_no_of_rooms` | bedrooms + bathrooms |
| `bath_per_bed` | bathrooms / (bedrooms + 1) |
| `room_per_bed` | total rooms / (bedrooms + 1) |
| `bed_x_bath` | bedrooms × bathrooms |
| `is_large` | Binary flag: total rooms ≥ 5 |

---

##  Modelling

Two models were trained and compared:

| Model | Notes |
|---|---|
| Linear Regression | Baseline; pipeline with `StandardScaler` |
| **Random Forest** | Chosen model; 100 estimators |

**Why Random Forest?** It handles non-linear relationships between features and price better than linear regression, and outperformed it on both training and test metrics.

**Target transformation:** `np.log1p()` was applied to the price target to correct right skew before training. Predictions are inverse-transformed with `np.expm1()` before display.

**Preprocessing pipeline:**
- `TargetEncoder` → `town`
- `OneHotEncoder` → `title`, `state`
- `passthrough` → numerical features

**Train/test split:** 80/20, `random_state=42`

---

## Model Performance

| Metric | Value |
|---|---|
| **R² Score** | *(0.5390)* |
| **Test MAE** | *(78,899,826)* |
| **RMSE** | *(164,722,650)* |

> Full evaluation results are in [`notebooks/Modelling_of_Nigerian_Dataset.ipynb`](notebooks/Modelling_of_Nigerian_Dataset.ipynb)

---

## Key EDA Findings

- **Abuja** has the highest average property prices making it the premium investment destination
- **Lagos** has more listings and a wider price range, better suited for volume investors
- **Detached Duplexes** dominate listings (6,335) but are also the most expensive per bedroom (~₦48M/bedroom)
- **Detached Bungalows** offer the best value at ~₦10M per bedroom
- Median market entry price: **₦75M** (25th percentile: ₦38M, 75th: ₦155M)

---

## App Features

The Streamlit app allows users to input:
- State (Lagos or Abuja)
- Town
- Property type (Detached Duplex, Semi-Detached Duplex, Terraced Duplex, Detached Bungalow, Semi-Detached Bungalow, Terraced Bungalow, Block of Flats)
- Number of bedrooms, bathrooms, and total rooms

And outputs an **instant price estimate in Naira**.

---

## Repository Structure

```
├── app.py                          # Streamlit app
├── model_rf.pkl                    # Trained Random Forest model
├── requirements.txt                # Dependencies
├── README.md
│
├── notebooks/
│   ├── EDA_on_Nigerian_real_estate.ipynb
│   ├── Modelling_of_Nigerian_Dataset.ipynb
│   └── Streamlit_Deployment.ipynb
│
└── data/
    └── nigeria_houses_data.csv     # Raw dataset (not tracked in git if large)
```

---

## Run Locally

```bash
git clone https://github.com/your-username/nigerian-house-price-predictor.git
cd nigerian-house-price-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## Tech Stack

`Python` · `pandas` · `scikit-learn` · `NumPy` · `Matplotlib` · `Seaborn` · `joblib` · `Streamlit`

---

## Author

**Faith Aduloju**  
[GitHub](https://github.com/adugbemi) 
[LinkedIn](https://linkedin.com/in/gbemisola-aduloju)