# Nigerian Real Estate Market Analysis

> An end-to-end exploratory data analysis of **24,326 Nigerian property listings**  answering real market questions for investors, developers, banks, and fintechs.

[View Notebook on nbviewer](Jupyter Notebook Viewer )  🔗 [LinkedIn](https://www.linkedin.com/in/gbemisola-aduloju-9b0380297/)

---

## Overview

Nigeria's property market is large, fragmented, and poorly understood at the data level. This project cuts through the noise by systematically analyzing listing data scraped from Nigerian real estate platforms to surface patterns in pricing, demand, and value across states and property types.

The analysis is structured around 10 concrete business questions not just charts covering investment decisions, market structure, risk signals, and developer strategy.

---

## Business Questions

| Stakeholder | Question |
|---|---|
| **Investor** | Where should I invest in Nigerian real estate? |
| **Investor** | Which property type gives the best value for money? |
| **Investor** | What is the realistic cost of entry? |
| **Market Analyst** | Which states have the most active listing markets? |
| **Market Analyst** | Is the market geographically concentrated or spread across Nigeria? |
| **Market Analyst** | What separates the affordable segment from the luxury segment? |
| **Risk / Compliance** | Are there outlier prices suggesting fraud or data quality issues? |
| **Risk / Compliance** | How much price variation exists within each state? |
| **Developer** | What property type should I build to maximize market absorption? |
| **Developer** | Which locations have the highest demonstrated demand? |

---

## Dataset

- **Source:** [Nigerian House Price Dataset](https://www.kaggle.com/datasets/michaelanietie/nigerian-house-price-dataset) — scraped from Nigerian real estate platforms
- **Raw size:** 24,326 listings · 8 features
- **Features:** `bedrooms`, `bathrooms`, `toilets`, `parking_space`, `title`, `town`, `state`, `price`
- **After cleaning:** 13,631 records (see Data Cleaning below)

---

## Data Cleaning

The raw dataset required significant cleaning before analysis:

| Issue | Detail | Action |
|---|---|---|
| **Duplicate listings** | 10,438 duplicates — 42.9% of the dataset, likely from repeated scraping cycles | Removed all duplicates → 13,888 unique records |
| **Price outliers** | Raw prices ranged from ₦90K to ₦1.8 trillion — extreme values are almost certainly data entry errors or scraping artifacts | Applied 1st–99th percentile filter → 257 records removed → 13,631 final records |

Post-cleaning, the price range is ₦6M–₦1.6B with a readable distribution centred around ₦75M.

---

## Key Findings

###  Market Structure
- **The market is a tale of two cities.** Lagos and Abuja together account for **84% of all listings**. The Nigerian property market is not geographically distributed — it is heavily concentrated in two states.
- Lagos dominates in **volume** (61% of listings), while Abuja commands the highest **average prices** (₦183M vs Lagos at ₦160M).
- Most other states have fewer than 500 listings, which limits data-driven conclusions about those markets.

###  Pricing

| Metric | Value |
|---|---|
| Minimum (after cleaning) | ₦6M |
| 25th Percentile — affordable entry | ₦38M |
| Median | ₦75M |
| 75th Percentile — luxury threshold | ₦155M |
| Maximum (after cleaning) | ₦1.6B |

- **Lagos and Abuja** have the widest price distributions; both premium and affordable listings coexist in these markets.
- **Other states** are cheaper and more tightly clustered, indicating less market variability but also lower liquidity.

### Location Demand
- **Lekki is the heartbeat of Nigerian real estate**;3,500+ listings in the cleaned dataset, nearly **3× more** than second-place Ajah.
- The top 5 demand locations are all in Lagos: Lekki, Ajah, Ikoyi, Ikeja, with Port Harcourt as the only non-Lagos entry in the top 5.
- For developers and investors, **Lekki and Ajah represent the highest-demand locations in the country**.

###  Property Type Supply
- **Detached Duplexes dominate** with 6,335 listings, nearly 4× more than any other type. This also signals **potential market saturation**.
- Developers seeking less competition may find better opportunities in Terraced Duplexes, Detached Bungalows, or Block of Flats each showing healthy demand (1,400–2,000 listings) without the same crowding.
- **Detached Duplexes command the highest average prices** overall, making them a premium rather than a value choice.

### Best Value Property
- **Detached Bungalows offer the best value for money** at approximately **₦10M per bedroom**, nearly **5× cheaper per bedroom** than Detached Duplexes (₦48M per bedroom).
- For budget-conscious buyers, bungalows deliver the most space per naira spent.

### Risk Signals
- Raw price data contained entries as low as ₦90K and as high as ₦1.8 trillion clear indicators of fraud, test listings, or scraping errors.
- After the quantile filter, 257 records (2%) were removed as price outliers.
- Price variation is highest in Lagos and Abuja, making due diligence on individual listings especially important in those markets.

### Feature Relationships ( Modeling Implications)
- **Bedrooms** is the strongest numeric predictor of price (correlation: **0.35**) but even this is only moderate, confirming that **location and property type are stronger price drivers than bedroom count alone**.
- **Bathrooms and toilets** are highly correlated with each other (**0.79**),only one should enter predictive models to avoid multicollinearity.
- **Parking space** has almost no relationship with price (**0.05**), likely droppable as a feature.

---

## Tools & Libraries

- Python 3
- Pandas: data wrangling, deduplication, aggregation
- NumPy: numerical operations
- Matplotlib & Seaborn: visualization

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/adugbemi/Analysis-on-Nigerian-Real-estate.git
cd Analysis-on-Nigerian-Real-estate

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn jupyter

# 3. Launch the notebook
jupyter notebook "EDA on Nigerian real estate.ipynb"
```

---


## Author

**Gbemi Adugbemi** — Data Analyst & ML Engineer  
[LinkedIn](https://www.linkedin.com/in/gbemisola-aduloju-9b0380297/) · [GitHub](https://github.com/adugbemi)
