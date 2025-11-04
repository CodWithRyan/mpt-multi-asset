# Mordern Portfolio Theory on Mutiple Assets

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt 

def read_csv():
    """ Charger les données depuis un fichier CSV """
    stock_prices = pd.read_csv('/Users/nkeniryanbonny/Documents/Modeles_lm/Quantitative Portfolio Management/data_modules/Capstone_data.csv', index_col=[0])
    stock_prices.index = pd.to_datetime(stock_prices.index, format='%d-%m-%Y')
    return stock_prices

def calculate_annual_returns(stock_prices):
    """ Calcul des rendements annualisés """
    annual_returns = ((((stock_prices.iloc[-1]-stock_prices.iloc[0]) / stock_prices.iloc[0]) + 1)**(252/len(stock_prices)) - 1)
    return annual_returns


def calculate_daily_returns(stock_prices):
    """ calcul des rendements journaliers """
    stock_returns = stock_prices.pct_change().dropna()
    return stock_returns

def generate_random_portfolios(stock_prices, annual_returns, stock_returns, num_of_portfolios=1000):
    """ Generate random portfolio
        Ensure the sum of weights is 1"""
    # create an empty dataframe and initialise the number of portfolio
    portfolio = pd.DataFrame()
    weights_array = []
    weights_array = []
    num_of_portfolios = 1000
    num_of_stocks = stock_prices.shape[1]

    for i in range(num_of_portfolios):
        rnd_nums = list(np.random.random(num_of_stocks))
        weights = list(rnd_nums/sum(rnd_nums))
        weights_array.append(weights)

        #save portfolio returns and portfolio std ddev values along with its ratio
        portfolio.loc[i, 'returns'] = sum(weights * annual_returns)
        #calculate the portfolio returns
        portfolio_rets = stock_returns * weights
        # Calculate the portfolio standard deviation
        portfolio.loc[i, 'std_dev'] = portfolio_rets.sum(axis=1).std()*math.sqrt(252)
        # Calculate the portfolio Sharpe 
        portfolio.loc[i, 'returns/std_dev'] = portfolio.loc[i, 'returns'] / portfolio.loc[i, 'std_dev']
    return portfolio, weights_array

def optimal_portfolios(portfolio, weights_array):
    """ Portfolio with maximum Sharpe Ratio
        Portfolio with minimum risk"""
    max_ret_by_std_dev = portfolio.iloc[portfolio['returns/std_dev'].idxmax()]
    wts_max_ret_by_std_dev = weights_array[portfolio['returns/std_dev'].idxmax()]

    min_std_dev = portfolio.iloc[portfolio['std_dev'].idxmin()]
    wts_min_std_dev = weights_array[portfolio['std_dev'].idxmin()]

    return max_ret_by_std_dev, wts_max_ret_by_std_dev, min_std_dev, wts_min_std_dev

def efficient_frontier(portfolio, max_ret_by_std_dev, min_std_dev):
    """ Highlight the maximum returns/risk portfolio and minimum risk portfolio """

    plt.figure(figsize=(10, 7))
    plt.grid()
    plt.scatter(portfolio.std_dev, portfolio.returns, label='Random Portfolios')
    plt.scatter(max_ret_by_std_dev.std_dev, max_ret_by_std_dev.returns,
                marker='*', s=200, color='r', label='Maximum Ret/Risk Portfolio')
    plt.scatter(min_std_dev.std_dev, min_std_dev.returns,
                marker='*', s=200, color='darkorange', label='Minimum Risk Portfolio')
    plt.xlabel('Portfolio Standard Deviation', fontsize=14)
    plt.xticks(fontsize=12)
    plt.ylabel('Portfolio Returns', fontsize=14)
    plt.yticks(fontsize=12)
    plt.legend(loc='best', fontsize=14)
    plt.title('Portfolio Optimization based on Efficient Frontier', fontsize=20)
    plt.savefig('notebooks/efficient_frontier.png', dpi=150, bbox_inches='tight')
    plt.show()

def print_portfolio_results(stock_prices, max_ret_by_std_dev, min_std_dev, wts_max_ret_by_std_dev, wts_min_std_dev):
    """
    Affiche les résultats de l'optimisation.
    """
   
    print("The portfolio metrics for the maximum return/std dev. portfolio:")
    print(max_ret_by_std_dev)
    print("\nThe portfolio weights for each stock in the maximum return/std dev. portfolio is as:")
    for i,j in zip(stock_prices.columns,wts_max_ret_by_std_dev):
        print("{} {}%".format(i,round(j*100,2))) 
    
    print("The portfolio metrics for the minimum std dev. portfolio:")
    print(min_std_dev)
    print("\nThe portfolio weights for each stock in the minimum std dev. portfolio is as:")
    for i,j in zip(stock_prices.columns,wts_min_std_dev):
        print("{} {}%".format(i,round(j*100,2))) 


