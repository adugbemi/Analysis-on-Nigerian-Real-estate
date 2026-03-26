# Nigerian Real Estate Market Analysis
An exploratory data analysis of 24,000+ Nigerian property listings, designed to answer key business questions for investors, developers, banks, and fintechs operating in the Nigerian property market.

## Key Findings
-  **Lagos vs Abuja** : Lagos dominates in volume (61% of listings) while Abuja commands the highest average prices
-  **Lekki**: is the most in-demand location with 3,500+ listings,nearly 3x more than second-place Ajah
-  **Detached Bungalows** :offer the best value at ₦10M per bedroom, nearly 5x cheaper than Detached Duplexes
-  **Median property price**: is ₦75M affordable entry starts at ₦38M

## Business Questions Answered
| Category | Question |
|---|---|
| Investment | Where should I invest in Nigerian real estate? |
| Investment | Which property type gives the best value for money? |
| Investment | What is the average cost of entry? |
| Market | Which states have the most active markets? |
| Market | Is the market concentrated or spread across Nigeria? |
| Market | What is the price range — affordable vs luxury? |
| Risk | Are there outlier prices suggesting fraud or data errors? |
| Risk | How much price variation exists within each state? |
| Developer | What type of property should I build to maximize sales? |
| Developer | Which locations have the most demand? |

## Tools & Libraries
- Python 3
- Pandas
- Matplotlib
- Seaborn
- NumPy

## How to Run
1. Clone the repo
2. Install dependencies : pip install -r requirements.txt
3. Open the notebook :jupyter notebook "EDA on Nigerian real estate.ipynb"

## Next Steps
- Price prediction model (Linear Regression → Random Forest → XGBoost)
- Property segmentation using KMeans clustering
- Interactive Streamlit price estimator

## Dataset
The dataset contains 24,326 Nigerian property listings with the following features:
bedrooms, bathrooms, toilets, parking_space, title, town, state, price
