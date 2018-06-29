# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:15:01 2018

@author: Caelum Kamps
"""

import numpy as np
from matplotlib import pyplot as plt

def plot_value(book, step = 1, fixed = 0.2):
    
    center = np.mean([leg.current_price for leg in book]) # What is book
    cp = center
    prices = [cp + i*step for i in range(-50,50)]
    values = []
    
    # Specifying prices to evalute at
    for price in prices:
        v = 0
        for leg in book:
            v += leg.get_t_value(price)*leg.contracts
        values.append(v)
        
    
    # Cacluating the breakeven point using the amount paid for the contracts
    paid = sum([leg.price_paid for leg in book])
    
    plt.grid()
    plt.title('Theoretical Portfolio value - Time Independent')
    plt.ylabel('Option Price ($)')
    plt.xlabel('Underlying Price ($)')
    for leg in book:
        plt.axvline(x=leg.strike, color = 'r', linestyle = 'dashdot', label = 'Strike')
    plt.axvline(x=leg.current_price, color = 'g', linestyle ='dashdot', label = 'Current')
   
    plt.axhline(paid, color = 'y', linestyle = 'dashdot', label = 'breakeven')
    plt.plot(prices,values)
    plt.legend()
    plt.show()
    
    # Calculating the current worth of the position
    current_worth = -paid
    for leg in book:
        current_worth += leg.t_value*leg.contracts
    print('Current worth = $',str(current_worth*100)[0:5])

def plot_delta(book, step):
    
    # Finding plot center
    center = np.mean([leg.current_price for leg in book])
    cp = center
    prices = [cp + i*step for i in range(-50,50)]
    deltas = []
    
    for price in prices:
        d = 0
        for leg in book:
            d+= leg.get_t_delta(price)
        deltas.append(d)
        
    plt.grid()
    plt.title('Theoretical Delta value - Time Independent')
    plt.ylabel('Delta')
    plt.xlabel('Underlying Price ($)')
   
    for leg in book:
        plt.axvline(x=leg.strike, color = 'r', linestyle = 'dashdot', label = 'Strike')
    plt.axvline(x=leg.current_price, color = 'g', linestyle ='dashdot', label = 'Current')
   
    plt.plot(prices,deltas)
    plt.legend()
    plt.show()

def plot_gamma(book, step):
    
    # Finding plot center
    center = np.mean([leg.current_price for leg in book])
    cp = center
    prices = [cp + i*step for i in range(-50,50)]
    gammas = []
    
    for price in prices:
        d = 0
        for leg in book:
            d+= leg.get_t_gamma(price)
        gammas.append(d)
        
    plt.grid()
    plt.title('Theoretical Gamma Value - Time Independent')
    plt.ylabel('Delta')
    plt.xlabel('Underlying Price ($)')
   
    for leg in book:
        plt.axvline(x=leg.strike, color = 'r', linestyle = 'dashdot', label = 'Strike')
    plt.axvline(x=leg.current_price, color = 'g', linestyle ='dashdot', label = 'Current')
   
    plt.plot(prices,gammas)
    plt.legend()
    plt.show()
    
