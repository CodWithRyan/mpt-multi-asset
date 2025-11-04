# Modern Portfolio Theory on Multiple Assets

## 🎯 Overview

We provide a model solution to implement the MPT on multiple assets.
The model solution here guides you to answer the problem statements posed in the project. The structure is as follows:

## 📖 Methodology

1) Import the data and calculate annualised returns.
2) Make random portfolios with different weights: Create a portfolio with random weights of the constituents. The portfolio metrics is calculated and saved in a data frame.
3) Identify the portfolios with maximum returns/risk and minimum risk: The portfolios with minimum risk and maximum Sharpe ratio (returns/risk) is selected from the list of random portfolios.
4) Efficient frontier: The efficient frontier is plotted for a visual representation of the various portfolios.
5) Results: The optimal weights are printed for the portfolios with minimum risk and maximum Sharpe ratio.

## 🛠️ Installation
```bash
pip install -r requirements.txt
```

## 📊 Data Sources
### Option 1: Using provided dataset
The project includes sample data in `data/raw/Capstone_data.csv` containing :
  - historical prices for 3 assets
  - period: 01/01/2016 - 31/12/2017
  - frequency: daily
### Option 2: Using Yahoo Finance


## 🚀 Quick start
- Open `notebooks/01_mpt_multi_asset_report.ipynb`
- Select the **mpt-multi-asset** kernel

## 📈 Results
Screenshots of charts

## 👤 Author
🧑🏽‍💻 Bonny Ryan Fotsing

